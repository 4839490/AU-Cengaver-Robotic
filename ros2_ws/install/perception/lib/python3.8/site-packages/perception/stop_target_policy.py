# perception/stop_target_policy.py
#
# S3-S1/S3-S2 — ROS-free policy helpers for stop_target_node.
#
# This module is intentionally ROS-free so that all freshness and evidence-
# evaluation logic can be unit-tested without a running ROS2 environment.
#
# The node passes plain Python values extracted from ROS messages into these
# functions; the functions return plain Python objects (None or StopEvidence).
#
# StopEvidence is the policy object for a single stop-evidence candidate.
# It carries NO driving-decision semantics and no /cmd_vel / /control / /beemobs
# semantics. The consumer (stop_target_node → planner/FSM) makes all decisions.
#
# S3-S2 additions:
#   - evaluate_light_stop_evidence() now accepts relevant_to_route and distance_m.
#   - Priority is CRITICAL when relevant_to_route=True, HIGH otherwise.
#   - StopEvidence carries distance_m for front-bumper-referenced geometry.
#   - build_stop_target_fields() maps StopEvidence → dict of StopTarget field values
#     (ROS-free; the node wraps this dict into a perception_msgs/StopTarget message).
#
# Contract references:
#   wiki/contracts/message_contracts.md §11 / §15 — StopTarget canonical schema
#   wiki/contracts/timing_and_fallback.md — valid_until_ms per topic
#   wiki/perception/stop_target_node.md — aggregator architecture
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track S

# ──────────────────────────────────────────────────────────────────────────────
# TrafficLightState.msg constants (must stay in sync with perception_msgs/msg)
# ──────────────────────────────────────────────────────────────────────────────
LIGHT_UNKNOWN = 0
LIGHT_RED = 1
LIGHT_YELLOW = 2
LIGHT_GREEN = 3
LIGHT_STALE = 4
LIGHT_CONFLICT = 5

# ──────────────────────────────────────────────────────────────────────────────
# TrafficSign.msg type constants
# ──────────────────────────────────────────────────────────────────────────────
SIGN_STOP = 1

# TrafficSign.msg event_status constants
SIGN_EVENT_NEW = 0
SIGN_EVENT_TRACKED = 1
SIGN_EVENT_ALREADY_HANDLED = 2
SIGN_EVENT_STALE = 3

# ──────────────────────────────────────────────────────────────────────────────
# StopTarget.msg constants (must stay in sync with perception_msgs/msg)
# ──────────────────────────────────────────────────────────────────────────────
TARGET_TRAFFIC_LIGHT_STOP = 0
TARGET_STOP_SIGN = 1

PRIORITY_LOW = 0
PRIORITY_NORMAL = 1
PRIORITY_HIGH = 2
PRIORITY_CRITICAL = 3

# Default freshness threshold (ms) — matches TrafficLightState valid_until_ms=300
DEFAULT_STALE_MS = 300

# StopTarget.msg valid_until_ms contract value (§11, §15).
STOP_TARGET_VALID_UNTIL_MS = 300


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def is_fresh(received_wall_s: float, now_wall_s: float, stale_ms: int) -> bool:
    """True if the wall-clock age of the most recent message is within stale_ms.

    received_wall_s: time.monotonic() value when the message callback fired.
                     Pass -1.0 (or any negative value) to signal "never received".
    now_wall_s:      time.monotonic() value at the time of evaluation.
    stale_ms:        maximum allowed age in milliseconds.
    """
    if received_wall_s < 0.0:
        return False
    age_ms = int((now_wall_s - received_wall_s) * 1000.0)
    return age_ms <= stale_ms


# ──────────────────────────────────────────────────────────────────────────────
# Policy object
# ──────────────────────────────────────────────────────────────────────────────

class StopEvidence:
    """Evidence object for a stop candidate.

    Carries no ROS types, no driving decisions, and no warning_flags field
    (StopTarget.msg contract §15 has no warning_flags field).

    Fields mirror the StopTarget.msg fields that the node populates when
    calling publish() in S3-S2+.
    """

    __slots__ = ('source_topic', 'target_type', 'priority', 'confidence',
                 'age_ms', 'distance_m')

    def __init__(
        self,
        source_topic: str,
        target_type: int,
        priority: int,
        confidence: float,
        age_ms: int,
        distance_m: float = 0.0,
    ) -> None:
        self.source_topic = source_topic
        self.target_type = target_type   # TARGET_TRAFFIC_LIGHT_STOP or TARGET_STOP_SIGN
        self.priority = priority          # PRIORITY_* constant
        self.confidence = confidence      # clamped to [0.0, 1.0]
        self.age_ms = age_ms             # from upstream message's age_ms field
        self.distance_m = distance_m     # front-bumper-referenced scalar (m); 0.0 when unknown


# ──────────────────────────────────────────────────────────────────────────────
# Evidence evaluation — traffic light
# ──────────────────────────────────────────────────────────────────────────────

def evaluate_light_stop_evidence(
    state: int,
    confirmed: bool,
    confidence: float,
    light_msg_age_ms: int,
    msg_valid_until_ms: int,
    light_received_wall_s: float,
    now_wall_s: float,
    stale_ms: int,
    relevant_to_route: bool = False,
    distance_m: float = 0.0,
) -> 'StopEvidence | None':
    """Evaluate TrafficLightState fields for actionable stop evidence.

    Returns a StopEvidence when confirmed RED light evidence is fresh.
    Returns None in all other cases (UNKNOWN / STALE / CONFLICT / YELLOW / GREEN /
    unconfirmed / wall-clock stale / message validity expired / never received).

    Priority rules (contract §Track S, S3-S2):
      relevant_to_route=True  → CRITICAL (3)
      relevant_to_route=False → HIGH (2)

    Arguments:
        state               TrafficLightState.state int (use LIGHT_* constants).
        confirmed           TrafficLightState.confirmed bool.
        confidence          TrafficLightState.confidence float.
        light_msg_age_ms    TrafficLightState.age_ms uint32 (from publisher).
        msg_valid_until_ms  TrafficLightState.valid_until_ms uint32 (normally 300).
        light_received_wall_s  time.monotonic() when the last callback fired (-1 = never).
        now_wall_s          time.monotonic() at evaluation time.
        stale_ms            Wall-clock freshness threshold in ms.
        relevant_to_route   TrafficLightState.relevant_to_route bool (S3-R4 wires this
                            from active_route_context; defaults to False = conservative).
        distance_m          TrafficLightState.distance_to_stop float (m); 0.0 when
                            route-context geometry is not yet available (Sprint 3 placeholder).
    """
    # Wall-clock freshness: did we receive a message recently enough?
    if not is_fresh(light_received_wall_s, now_wall_s, stale_ms):
        return None

    # Message validity: has the message's own validity window expired?
    if light_msg_age_ms > msg_valid_until_ms:
        return None

    # Only confirmed RED generates stop evidence.
    # UNKNOWN / STALE / CONFLICT / YELLOW / GREEN → no evidence.
    if state != LIGHT_RED or not confirmed:
        return None

    # S3-S2 priority: CRITICAL when route context confirms relevance, HIGH otherwise.
    priority = PRIORITY_CRITICAL if relevant_to_route else PRIORITY_HIGH

    return StopEvidence(
        source_topic='/perception/traffic_light_state',
        target_type=TARGET_TRAFFIC_LIGHT_STOP,
        priority=priority,
        confidence=max(0.0, min(1.0, confidence)),
        age_ms=light_msg_age_ms,
        distance_m=max(0.0, distance_m),
    )


# ──────────────────────────────────────────────────────────────────────────────
# Evidence evaluation — traffic signs
# ──────────────────────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────────────────────
# StopTarget field builder — pure function, ROS-free
# ──────────────────────────────────────────────────────────────────────────────

def build_stop_target_fields(
    evidence: StopEvidence,
    now_age_ms: int = 0,
) -> 'dict | None':
    """Map StopEvidence to a dict of perception_msgs/StopTarget field values.

    Returns None when the combined age (evidence.age_ms + now_age_ms) exceeds
    STOP_TARGET_VALID_UNTIL_MS — the caller must not publish in that case.
    Clamping stale evidence into validity would produce a StopTarget that looks
    fresh to consumers but is backed by expired data.

    Pure function — no ROS types. The node uses this dict to populate a
    perception_msgs/StopTarget message before calling publish().

    now_age_ms: wall-clock delta (ms) accumulated in the node since the last
                upstream message was received.

    Geometry placeholder note (S3-S2): distance_from_front_bumper mirrors
    TrafficLightState.distance_to_stop which is 0.0 until route-context geometry
    is wired in Track R (S3-R4). target_x and target_y are 0.0 for the same
    reason. Planner must treat these as evidence placeholders until stop-line
    geometry is available. See wiki/perception/stop_target_node.md §StopTarget
    field highlights.

    No warning_flags key: StopTarget.msg contract §15 omits warning_flags.
    """
    age_ms = evidence.age_ms + now_age_ms
    if age_ms > STOP_TARGET_VALID_UNTIL_MS:
        return None
    return {
        'target_type': evidence.target_type,
        'distance_from_front_bumper': evidence.distance_m,
        'target_x': 0.0,
        'target_y': 0.0,
        'confidence': evidence.confidence,
        'source': 'perception_only',
        'age_ms': age_ms,
        'valid_until_ms': STOP_TARGET_VALID_UNTIL_MS,
        'waypoint_id': -1,
        'heading_at_stop': 0.0,
        'priority': evidence.priority,
        'required_stop_duration_ms': 0,
        'stop_reason_id': 0,
        'source_topic': evidence.source_topic,
    }


def has_stop_sign_evidence(
    signs: list,
    signs_received_wall_s: float,
    now_wall_s: float,
    stale_ms: int,
) -> bool:
    """True if any sign is a fresh, confirmed STOP sign with actionable event_status.

    A STOP sign is actionable when ALL of the following hold:
      1. The TrafficSigns wrapper wall-clock age is within stale_ms.
      2. sign.type == SIGN_STOP.
      3. sign.event_status is NEW or TRACKED.
      4. sign.confirmed is True.
      5. sign.age_ms and sign.valid_until_ms are both present, valid_until_ms > 0,
         and sign.age_ms <= sign.valid_until_ms.

    If a sign is missing age_ms or valid_until_ms fields it is treated as
    invalid/stale rather than actionable.

    relevant_to_route is NOT required in S3-S1. Route gating is deferred to
    S3-S2 / Track R when /planning/active_route_context is wired.

    S3-S1 note: stop_target_node evaluates this but does NOT publish for sign
    evidence. Sign-sourced StopTarget construction is deferred to S3-S2.

    signs: list of objects with TrafficSign.msg field names
           (ROS msgs or plain SimpleNamespace for tests).
    signs_received_wall_s: time.monotonic() when the last TrafficSigns callback fired.
    """
    if not is_fresh(signs_received_wall_s, now_wall_s, stale_ms):
        return False

    for sign in signs:
        sign_type = getattr(sign, 'type', -1)
        event_status = getattr(sign, 'event_status', SIGN_EVENT_STALE)
        confirmed = getattr(sign, 'confirmed', False)
        age_ms = getattr(sign, 'age_ms', None)
        sign_valid_until_ms = getattr(sign, 'valid_until_ms', None)

        # Reject wrong type or non-actionable event status first (cheap checks).
        if sign_type != SIGN_STOP:
            continue
        if event_status not in (SIGN_EVENT_NEW, SIGN_EVENT_TRACKED):
            continue

        # Must be confirmed by the sign node (3-frame equivalent for signs).
        if not confirmed:
            continue

        # Per-sign validity: both fields must be present and the sign must not
        # have expired. Missing fields → treat as invalid/stale.
        if age_ms is None or sign_valid_until_ms is None:
            continue
        # valid_until_ms=0 indicates validity not set → treat as invalid.
        if sign_valid_until_ms <= 0:
            continue
        if age_ms > sign_valid_until_ms:
            continue

        return True

    return False

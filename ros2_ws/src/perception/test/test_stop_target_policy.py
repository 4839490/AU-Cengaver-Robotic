# test/test_stop_target_policy.py
#
# S3-S1/S3-S2 — ROS-free unit tests for stop_target_policy.py.
#
# All tests run without a ROS2 environment. TrafficSign-like objects are
# constructed with types.SimpleNamespace so no perception_msgs import is needed.
#
# Test coverage:
#   is_fresh() [5 tests]:
#     - never received (-1.0) → False
#     - fresh (within stale_ms) → True
#     - at boundary → True
#     - over boundary → False
#     - clearly stale → False
#
#   evaluate_light_stop_evidence() [14 tests — S3-S1: 11, S3-S2: 3 new]:
#     - no light ever received → None
#     - stale light (wall clock) → None
#     - UNKNOWN state → None
#     - STALE state → None
#     - CONFLICT state → None
#     - GREEN → None
#     - YELLOW (confirmed) → None (YELLOW deferred)
#     - RED + unconfirmed → None
#     - message validity expired (age_ms > valid_until_ms) → None
#     - confirmed RED + fresh → StopEvidence
#     - StopEvidence has NO warning_flags attribute (contract §15)
#     - confidence clamped to [0.0, 1.0] (2 tests)
#     [S3-S2 new]:
#     - confirmed RED + relevant_to_route=True → priority=CRITICAL
#     - confirmed RED + relevant_to_route=False (default) → priority=HIGH
#     - confirmed RED + distance_m → StopEvidence.distance_m preserved
#
#   build_stop_target_fields() [11 tests — new in S3-S2; Codex-fixed in S3-S2-fix]:
#     - target_type=0 (TRAFFIC_LIGHT_STOP)
#     - priority=3 (CRITICAL) for CRITICAL evidence
#     - valid_until_ms=300
#     - source_topic="/perception/traffic_light_state"
#     - source="perception_only"
#     - waypoint_id=-1
#     - age_ms = evidence.age_ms + now_age_ms when sum <= valid_until_ms
#     - returns None when combined_age_ms > valid_until_ms (Codex fix: no stale clamp)
#     - combined age at boundary (200+100=300) → publishable, age_ms=300
#     - no 'warning_flags' key in returned dict
#     - confidence preserved from evidence
#
#   has_stop_sign_evidence() [15 tests]:
#     - signs never received → False
#     - stale signs (wall clock) → False
#     - empty signs list → False
#     - non-STOP sign type → False
#     - STOP sign with ALREADY_HANDLED event_status → False
#     - STOP sign with STALE event_status → False
#     - STOP sign NEW confirmed=False → False
#     - STOP sign TRACKED confirmed=True age > valid_until → False
#     - STOP sign TRACKED confirmed=True age == valid_until → True
#     - STOP sign NEW missing age_ms → False
#     - STOP sign NEW missing valid_until_ms → False
#     - STOP sign NEW valid_until_ms=0 → False
#     - STOP sign with NEW confirmed=True fresh → True
#     - STOP sign with TRACKED confirmed=True fresh → True
#     - multiple signs with one valid STOP NEW → True
#
# Total: 45 tests (33 S3-S1 + 12 S3-S2: 11 original + 1 Codex fix).

from types import SimpleNamespace
import pytest

from perception.stop_target_policy import (
    LIGHT_UNKNOWN,
    LIGHT_RED,
    LIGHT_YELLOW,
    LIGHT_GREEN,
    LIGHT_STALE,
    LIGHT_CONFLICT,
    SIGN_STOP,
    SIGN_EVENT_NEW,
    SIGN_EVENT_TRACKED,
    SIGN_EVENT_ALREADY_HANDLED,
    SIGN_EVENT_STALE,
    TARGET_TRAFFIC_LIGHT_STOP,
    PRIORITY_HIGH,
    PRIORITY_CRITICAL,
    STOP_TARGET_VALID_UNTIL_MS,
    is_fresh,
    evaluate_light_stop_evidence,
    build_stop_target_fields,
    has_stop_sign_evidence,
    StopEvidence,
)

# ──────────────────────────────────────────────────────────────────────────────
# Shared test fixtures (plain floats — no ROS clock needed)
# ──────────────────────────────────────────────────────────────────────────────
NOW = 1000.0        # arbitrary wall-clock second
STALE_MS = 300
VALID_UNTIL_MS = 300
FRESH_WALL_S = NOW - 0.100   # 100 ms ago → fresh
STALE_WALL_S = NOW - 0.400   # 400 ms ago → stale (> 300 ms)
NEVER = -1.0                  # sentinel: message never received


def _eval_light(state, confirmed, confidence=0.9, age_ms=50,
                valid_until_ms=VALID_UNTIL_MS, received_wall_s=FRESH_WALL_S):
    """Convenience wrapper to reduce repetition in light evidence tests."""
    return evaluate_light_stop_evidence(
        state=state,
        confirmed=confirmed,
        confidence=confidence,
        light_msg_age_ms=age_ms,
        msg_valid_until_ms=valid_until_ms,
        light_received_wall_s=received_wall_s,
        now_wall_s=NOW,
        stale_ms=STALE_MS,
    )


def _sign(type_, event_status, confirmed=False, age_ms=None, valid_until_ms=None):
    """Build a sign-like object matching TrafficSign.msg field names.

    confirmed, age_ms, valid_until_ms default to values that make the sign
    NOT actionable unless explicitly supplied — this keeps False-expecting tests
    concise while requiring True-expecting tests to be explicit about validity.
    """
    return SimpleNamespace(
        type=type_,
        event_status=event_status,
        confirmed=confirmed,
        age_ms=age_ms,
        valid_until_ms=valid_until_ms,
    )


def _valid_stop_sign(event_status=SIGN_EVENT_NEW):
    """A fully-valid STOP sign for positive-case tests (all required fields set)."""
    return _sign(SIGN_STOP, event_status, confirmed=True, age_ms=50, valid_until_ms=1000)


# ══════════════════════════════════════════════════════════════════════════════
# is_fresh()
# ══════════════════════════════════════════════════════════════════════════════

class TestIsFresh:

    def test_never_received_returns_false(self):
        """received_wall_s=-1.0 (never received) → False."""
        assert not is_fresh(NEVER, NOW, STALE_MS)

    def test_just_received_returns_true(self):
        """1 ms ago → fresh."""
        assert is_fresh(NOW - 0.001, NOW, STALE_MS)

    def test_at_boundary_returns_true(self):
        """Exactly at stale_ms boundary → fresh (inclusive)."""
        assert is_fresh(NOW - 0.300, NOW, STALE_MS)

    def test_one_ms_over_boundary_returns_false(self):
        """1 ms past the boundary → stale."""
        assert not is_fresh(NOW - 0.301, NOW, STALE_MS)

    def test_clearly_stale_returns_false(self):
        """400 ms ago → stale."""
        assert not is_fresh(STALE_WALL_S, NOW, STALE_MS)


# ══════════════════════════════════════════════════════════════════════════════
# evaluate_light_stop_evidence()
# ══════════════════════════════════════════════════════════════════════════════

class TestEvaluateLightStopEvidence:

    # ── No-evidence cases (node must NOT publish for any of these) ──────────

    def test_no_light_ever_received_returns_none(self):
        """No traffic light message ever received → no target."""
        assert _eval_light(LIGHT_UNKNOWN, False, received_wall_s=NEVER) is None

    def test_stale_wall_clock_returns_none(self):
        """Message received 400 ms ago (> stale_ms=300) → no target."""
        assert _eval_light(LIGHT_RED, True, received_wall_s=STALE_WALL_S) is None

    def test_unknown_state_returns_none(self):
        """state=UNKNOWN → no target."""
        assert _eval_light(LIGHT_UNKNOWN, False) is None

    def test_stale_state_returns_none(self):
        """state=STALE → no target."""
        assert _eval_light(LIGHT_STALE, False) is None

    def test_conflict_state_returns_none(self):
        """state=CONFLICT → no target."""
        assert _eval_light(LIGHT_CONFLICT, False) is None

    def test_green_state_returns_none(self):
        """state=GREEN → no target (green light = go, no stop needed)."""
        assert _eval_light(LIGHT_GREEN, True) is None

    def test_yellow_confirmed_returns_none(self):
        """state=YELLOW even with confirmed=True → no target in S3-S1 (YELLOW deferred)."""
        assert _eval_light(LIGHT_YELLOW, True) is None

    def test_unconfirmed_red_returns_none(self):
        """state=RED but confirmed=False → no target (S3-S1 scope: only confirmed RED)."""
        assert _eval_light(LIGHT_RED, confirmed=False) is None

    def test_msg_validity_expired_returns_none(self):
        """age_ms > valid_until_ms (message validity window expired) → no target."""
        assert _eval_light(LIGHT_RED, True, age_ms=400, valid_until_ms=300) is None

    # ── Confirmed RED case (policy object returned; node does NOT publish in S3-S1) ──

    def test_confirmed_red_fresh_returns_evidence(self):
        """Confirmed RED with fresh message → StopEvidence policy object.

        S3-S1: stop_target_node evaluates this result but does NOT call publish().
        S3-S2 will wire the publish() call.
        """
        result = _eval_light(LIGHT_RED, confirmed=True, confidence=0.85)
        assert result is not None
        assert isinstance(result, StopEvidence)
        assert result.target_type == TARGET_TRAFFIC_LIGHT_STOP
        assert result.source_topic == '/perception/traffic_light_state'
        assert abs(result.confidence - 0.85) < 1e-5
        assert result.priority == PRIORITY_HIGH  # S3-S1 default; S3-S2 upgrades to CRITICAL

    def test_confirmed_red_evidence_has_no_warning_flags(self):
        """StopEvidence has NO warning_flags attribute.

        StopTarget.msg contract §15 raw .msg block omits warning_flags.
        The policy object must not introduce this field either.
        """
        result = _eval_light(LIGHT_RED, confirmed=True)
        assert result is not None
        assert not hasattr(result, 'warning_flags')

    def test_confidence_clamped_above_one(self):
        """Confidence > 1.0 in the message is clamped to 1.0 in StopEvidence."""
        result = _eval_light(LIGHT_RED, True, confidence=1.5)
        assert result is not None
        assert result.confidence <= 1.0

    def test_confidence_clamped_below_zero(self):
        """Confidence < 0.0 in the message is clamped to 0.0 in StopEvidence."""
        result = _eval_light(LIGHT_RED, True, confidence=-0.5)
        assert result is not None
        assert result.confidence >= 0.0

    # ── S3-S2: priority from relevant_to_route ─────────────────────────────

    def test_confirmed_red_relevant_to_route_true_returns_critical(self):
        """Confirmed RED with relevant_to_route=True → priority=CRITICAL (3)."""
        result = evaluate_light_stop_evidence(
            state=LIGHT_RED, confirmed=True, confidence=0.9,
            light_msg_age_ms=50, msg_valid_until_ms=VALID_UNTIL_MS,
            light_received_wall_s=FRESH_WALL_S, now_wall_s=NOW,
            stale_ms=STALE_MS, relevant_to_route=True,
        )
        assert result is not None
        assert result.priority == PRIORITY_CRITICAL

    def test_confirmed_red_relevant_to_route_false_returns_high(self):
        """Confirmed RED with relevant_to_route=False (default) → priority=HIGH (2)."""
        result = evaluate_light_stop_evidence(
            state=LIGHT_RED, confirmed=True, confidence=0.9,
            light_msg_age_ms=50, msg_valid_until_ms=VALID_UNTIL_MS,
            light_received_wall_s=FRESH_WALL_S, now_wall_s=NOW,
            stale_ms=STALE_MS, relevant_to_route=False,
        )
        assert result is not None
        assert result.priority == PRIORITY_HIGH

    def test_confirmed_red_distance_m_preserved(self):
        """distance_m passed to evaluate_light_stop_evidence is carried in StopEvidence."""
        result = evaluate_light_stop_evidence(
            state=LIGHT_RED, confirmed=True, confidence=0.9,
            light_msg_age_ms=50, msg_valid_until_ms=VALID_UNTIL_MS,
            light_received_wall_s=FRESH_WALL_S, now_wall_s=NOW,
            stale_ms=STALE_MS, distance_m=7.5,
        )
        assert result is not None
        assert abs(result.distance_m - 7.5) < 1e-5


# ══════════════════════════════════════════════════════════════════════════════
# build_stop_target_fields() — S3-S2
# ══════════════════════════════════════════════════════════════════════════════

def _critical_red_evidence(confidence=0.85, age_ms=50, distance_m=0.0):
    """Build a CRITICAL confirmed-RED StopEvidence for build_stop_target_fields tests."""
    return StopEvidence(
        source_topic='/perception/traffic_light_state',
        target_type=TARGET_TRAFFIC_LIGHT_STOP,
        priority=PRIORITY_CRITICAL,
        confidence=confidence,
        age_ms=age_ms,
        distance_m=distance_m,
    )


class TestBuildStopTargetFields:

    def test_target_type_is_traffic_light_stop(self):
        """build_stop_target_fields returns target_type=0 (TRAFFIC_LIGHT_STOP)."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['target_type'] == TARGET_TRAFFIC_LIGHT_STOP
        assert fields['target_type'] == 0

    def test_priority_critical_preserved(self):
        """Priority from CRITICAL evidence is preserved in fields dict."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['priority'] == PRIORITY_CRITICAL
        assert fields['priority'] == 3

    def test_valid_until_ms_is_300(self):
        """valid_until_ms=300 per StopTarget contract §11/§15."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['valid_until_ms'] == STOP_TARGET_VALID_UNTIL_MS
        assert fields['valid_until_ms'] == 300

    def test_source_topic_correct(self):
        """source_topic matches the upstream traffic light topic."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['source_topic'] == '/perception/traffic_light_state'

    def test_source_perception_only(self):
        """source='perception_only' for sensor-only targets (no GeoJSON in S3)."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['source'] == 'perception_only'

    def test_waypoint_id_minus_one(self):
        """waypoint_id=-1: PICKUP/DROPOFF GeoJSON not in Sprint 3."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert fields['waypoint_id'] == -1

    def test_age_ms_sum_within_valid_until(self):
        """age_ms = evidence.age_ms + now_age_ms when sum <= valid_until_ms."""
        ev = _critical_red_evidence(age_ms=50)
        fields = build_stop_target_fields(ev, now_age_ms=100)
        assert fields['age_ms'] == 150

    def test_combined_age_exceeds_valid_until_returns_none(self):
        """evidence.age_ms=200 + now_age_ms=200 = 400 > 300 → None (do not publish stale evidence)."""
        ev = _critical_red_evidence(age_ms=200)
        result = build_stop_target_fields(ev, now_age_ms=200)
        assert result is None

    def test_combined_age_at_boundary_is_publishable(self):
        """evidence.age_ms=200 + now_age_ms=100 = 300 ≤ valid_until_ms → publishable, age_ms=300."""
        ev = _critical_red_evidence(age_ms=200)
        fields = build_stop_target_fields(ev, now_age_ms=100)
        assert fields is not None
        assert fields['age_ms'] == 300

    def test_no_warning_flags_key_in_fields(self):
        """No 'warning_flags' key: StopTarget.msg contract §15 omits this field."""
        fields = build_stop_target_fields(_critical_red_evidence())
        assert 'warning_flags' not in fields

    def test_confidence_preserved_from_evidence(self):
        """Confidence value from evidence is carried into fields dict unchanged."""
        ev = _critical_red_evidence(confidence=0.92)
        fields = build_stop_target_fields(ev)
        assert abs(fields['confidence'] - 0.92) < 1e-5


# ══════════════════════════════════════════════════════════════════════════════
# has_stop_sign_evidence()
# ══════════════════════════════════════════════════════════════════════════════

class TestHasStopSignEvidence:

    # ── Wrapper-level no-evidence cases (fail before per-sign checks) ───────

    def test_signs_never_received_returns_false(self):
        """No TrafficSigns message ever received → no target."""
        assert not has_stop_sign_evidence([], NEVER, NOW, STALE_MS)

    def test_stale_signs_wall_clock_returns_false(self):
        """TrafficSigns received 400 ms ago (> stale_ms) → no target."""
        stop = _valid_stop_sign()
        assert not has_stop_sign_evidence([stop], STALE_WALL_S, NOW, STALE_MS)

    def test_empty_signs_list_returns_false(self):
        """Empty signs[] wrapper (fresh) → no target."""
        assert not has_stop_sign_evidence([], FRESH_WALL_S, NOW, STALE_MS)

    # ── Per-sign type / event-status rejections ─────────────────────────────

    def test_non_stop_sign_type_returns_false(self):
        """SPEED_LIMIT sign (type=2) with NEW event_status → not a stop target."""
        speed_limit = _sign(type_=2, event_status=SIGN_EVENT_NEW)
        assert not has_stop_sign_evidence([speed_limit], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_already_handled_returns_false(self):
        """STOP sign with ALREADY_HANDLED event_status → not actionable."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_ALREADY_HANDLED)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_stale_event_returns_false(self):
        """STOP sign with STALE event_status → not actionable."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_STALE)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    # ── Per-sign confirmed check (new in Codex fix) ──────────────────────────

    def test_stop_sign_unconfirmed_returns_false(self):
        """STOP NEW but confirmed=False → not actionable.

        sign.confirmed must be True; unconfirmed detection is not stop evidence.
        """
        sign = _sign(SIGN_STOP, SIGN_EVENT_NEW, confirmed=False,
                     age_ms=50, valid_until_ms=1000)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    # ── Per-sign validity checks (new in Codex fix) ──────────────────────────

    def test_stop_sign_missing_age_ms_returns_false(self):
        """STOP NEW confirmed but age_ms field absent → treated as invalid/stale."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_NEW, confirmed=True,
                     age_ms=None, valid_until_ms=1000)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_missing_valid_until_ms_returns_false(self):
        """STOP NEW confirmed but valid_until_ms field absent → treated as invalid/stale."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_NEW, confirmed=True,
                     age_ms=50, valid_until_ms=None)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_zero_valid_until_ms_returns_false(self):
        """STOP NEW confirmed but valid_until_ms=0 → validity not set, treated as invalid."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_NEW, confirmed=True,
                     age_ms=0, valid_until_ms=0)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_expired_age_returns_false(self):
        """STOP TRACKED confirmed but age_ms > valid_until_ms → sign has expired."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_TRACKED, confirmed=True,
                     age_ms=1001, valid_until_ms=1000)
        assert not has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_at_validity_boundary_returns_true(self):
        """STOP TRACKED confirmed with age_ms == valid_until_ms → still fresh (inclusive)."""
        sign = _sign(SIGN_STOP, SIGN_EVENT_TRACKED, confirmed=True,
                     age_ms=1000, valid_until_ms=1000)
        assert has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    # ── Full positive cases (all checks must pass) ───────────────────────────

    def test_stop_sign_new_confirmed_fresh_returns_true(self):
        """STOP NEW confirmed=True with valid age → has actionable evidence."""
        sign = _valid_stop_sign(SIGN_EVENT_NEW)
        assert has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_stop_sign_tracked_confirmed_fresh_returns_true(self):
        """STOP TRACKED confirmed=True with valid age → has actionable evidence."""
        sign = _valid_stop_sign(SIGN_EVENT_TRACKED)
        assert has_stop_sign_evidence([sign], FRESH_WALL_S, NOW, STALE_MS)

    def test_multiple_signs_one_valid_stop_new_returns_true(self):
        """Multiple signs including one fully-valid STOP NEW → evidence detected."""
        signs = [
            _sign(type_=2, event_status=SIGN_EVENT_NEW),   # SPEED_LIMIT (non-stop)
            _valid_stop_sign(SIGN_EVENT_NEW),                # valid STOP
        ]
        assert has_stop_sign_evidence(signs, FRESH_WALL_S, NOW, STALE_MS)

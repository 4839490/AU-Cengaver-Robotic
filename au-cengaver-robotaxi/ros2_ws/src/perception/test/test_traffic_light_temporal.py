# test/test_traffic_light_temporal.py
#
# Sprint 1 / S1-5 — Unit tests for the pure-Python temporal confirmation filter.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (after `colcon build` + `source install/setup.bash`):
#   pytest cengaver_ws/src/perception/test/test_traffic_light_temporal.py -v
#
# Run through colcon:
#   colcon test --packages-select perception
#   colcon test-result --verbose

from perception.temporal_filter import TemporalFilter

_UNKNOWN = 0
_RED = 1
_YELLOW = 2
_GREEN = 3

_T0 = 0
_DT = 100  # 100 ms per frame → 10 Hz


# ------------------------------------------------------------------
# Required case 1: three consecutive RED → confirmed=True on third frame
# ------------------------------------------------------------------

def test_three_consecutive_red_confirms():
    f = TemporalFilter(confirm_frames=3)
    state, confirmed = f.update(_RED, _T0)
    assert state == _RED and not confirmed

    state, confirmed = f.update(_RED, _T0 + _DT)
    assert state == _RED and not confirmed

    state, confirmed = f.update(_RED, _T0 + 2 * _DT)
    assert state == _RED and confirmed


# ------------------------------------------------------------------
# Required case 2: RED then GREEN resets confirmation
# ------------------------------------------------------------------

def test_state_change_resets_confirmation():
    f = TemporalFilter(confirm_frames=3)
    for i in range(3):
        f.update(_RED, _T0 + i * _DT)
    # Filter is now confirmed RED; feed GREEN
    state, confirmed = f.update(_GREEN, _T0 + 3 * _DT)
    assert state == _GREEN
    assert not confirmed
    assert f.count == 1


# ------------------------------------------------------------------
# Required case 3: UNKNOWN resets confirmation
# ------------------------------------------------------------------

def test_unknown_resets_confirmation():
    f = TemporalFilter(confirm_frames=3)
    for i in range(3):
        f.update(_RED, _T0 + i * _DT)
    # Inject UNKNOWN
    state, confirmed = f.update(_UNKNOWN, _T0 + 3 * _DT)
    assert state == _UNKNOWN
    assert not confirmed
    assert f.count == 0
    assert f.accumulated_state == _UNKNOWN


# ------------------------------------------------------------------
# Required case 4: stale/no-input path resets confirmation
# ------------------------------------------------------------------

def test_explicit_reset_clears_filter():
    """Simulate stale-image path: node calls filter.reset()."""
    f = TemporalFilter(confirm_frames=3)
    for i in range(3):
        f.update(_RED, _T0 + i * _DT)
    assert f.confirmed

    f.reset()
    assert f.accumulated_state == _UNKNOWN
    assert f.count == 0
    assert not f.confirmed

    # After reset, next classification starts the count from 1
    state, confirmed = f.update(_RED, _T0 + 1000)
    assert state == _RED and not confirmed
    assert f.count == 1


# ------------------------------------------------------------------
# Required case 5: confirm_frames parameter is honored
# ------------------------------------------------------------------

def test_confirm_frames_2():
    f = TemporalFilter(confirm_frames=2)
    _, confirmed = f.update(_GREEN, _T0)
    assert not confirmed

    state, confirmed = f.update(_GREEN, _T0 + _DT)
    assert state == _GREEN and confirmed


def test_confirm_frames_5():
    f = TemporalFilter(confirm_frames=5)
    for i in range(4):
        _, confirmed = f.update(_YELLOW, _T0 + i * _DT)
        assert not confirmed

    _, confirmed = f.update(_YELLOW, _T0 + 4 * _DT)
    assert confirmed


# ------------------------------------------------------------------
# State-memory expiry
# ------------------------------------------------------------------

def test_state_memory_expiry_resets_count():
    f = TemporalFilter(confirm_frames=3, state_memory_ms=200)
    f.update(_RED, 0)
    f.update(_RED, 100)  # count=2
    # Elapsed=300 ms > state_memory_ms=200 → filter resets before accumulating
    state, confirmed = f.update(_RED, 400)
    assert state == _RED
    assert not confirmed
    assert f.count == 1  # started fresh after expiry


def test_update_within_memory_window_continues():
    f = TemporalFilter(confirm_frames=3, state_memory_ms=500)
    f.update(_GREEN, 0)
    f.update(_GREEN, 200)   # count=2, elapsed=200 ≤ 500 → no expiry
    state, confirmed = f.update(_GREEN, 400)   # count=3, elapsed=200 ≤ 500
    assert state == _GREEN and confirmed


# ------------------------------------------------------------------
# YELLOW confirms (exercise non-RED/GREEN path)
# ------------------------------------------------------------------

def test_yellow_three_frames_confirms():
    f = TemporalFilter(confirm_frames=3)
    for i in range(2):
        _, confirmed = f.update(_YELLOW, _T0 + i * _DT)
        assert not confirmed
    _, confirmed = f.update(_YELLOW, _T0 + 2 * _DT)
    assert confirmed


# ------------------------------------------------------------------
# Filter stays confirmed after further frames of the same state
# ------------------------------------------------------------------

def test_confirmed_stays_true_on_continued_frames():
    f = TemporalFilter(confirm_frames=3)
    for i in range(5):
        state, confirmed = f.update(_RED, _T0 + i * _DT)
    assert state == _RED and confirmed
    assert f.count == 5


# ------------------------------------------------------------------
# confirm_frames=1 edge case
# ------------------------------------------------------------------

def test_confirm_frames_1():
    f = TemporalFilter(confirm_frames=1)
    state, confirmed = f.update(_RED, _T0)
    assert state == _RED and confirmed


# ------------------------------------------------------------------
# Initial state before any update
# ------------------------------------------------------------------

def test_initial_state():
    f = TemporalFilter()
    assert f.accumulated_state == _UNKNOWN
    assert f.count == 0
    assert not f.confirmed


# ------------------------------------------------------------------
# S1-6 required cases: no-image-ever and stale-image paths
# ------------------------------------------------------------------

def test_no_image_ever_path_confirmed_false():
    """Case 1 equivalent: node never received an image → filter stays UNKNOWN.

    The node calls reset() on every tick when no image has arrived.  A filter
    that has never been updated (or was just reset) must never be confirmed.
    """
    f = TemporalFilter(confirm_frames=3)
    # Simulate repeated no-image ticks: node calls reset() each time
    for _ in range(10):
        f.reset()
    assert f.accumulated_state == _UNKNOWN
    assert f.count == 0
    assert not f.confirmed


def test_stale_image_path_resets_confirmation():
    """Case 2/3 equivalent: image becomes stale → node calls reset() → confirmed=False.

    Confirm that previously-confirmed state is cleared by reset(), matching
    the Case 2 (stale image) branch in traffic_light_node._tick().
    """
    f = TemporalFilter(confirm_frames=3)
    for i in range(3):
        f.update(_RED, _T0 + i * _DT)
    assert f.confirmed  # was confirmed before stale

    # Simulate stale-image tick: node calls _reset_filter() → filter.reset()
    f.reset()
    assert not f.confirmed
    assert f.accumulated_state == _UNKNOWN
    assert f.count == 0

    # Next fresh classification starts accumulating from count=1 (unconfirmed)
    state, confirmed = f.update(_RED, _T0 + 1000)
    assert state == _RED and not confirmed
    assert f.count == 1


def test_fresh_red_classifies_correctly_post_stale():
    """After a stale-induced reset, fresh frames re-confirm correctly."""
    f = TemporalFilter(confirm_frames=3)
    # Simulate stale event
    f.reset()
    # Fresh frames arrive again
    for i in range(2):
        _, confirmed = f.update(_GREEN, _T0 + i * _DT)
        assert not confirmed
    _, confirmed = f.update(_GREEN, _T0 + 2 * _DT)
    assert confirmed


def test_confirmed_true_only_after_filter_threshold():
    """confirmed=True must not appear before confirm_frames frames."""
    f = TemporalFilter(confirm_frames=3)
    for i in range(2):
        _, confirmed = f.update(_YELLOW, _T0 + i * _DT)
        assert not confirmed, f'confirmed=True after only {i+1} frame(s)'
    _, confirmed = f.update(_YELLOW, _T0 + 2 * _DT)
    assert confirmed, 'confirmed=False after 3 frames'

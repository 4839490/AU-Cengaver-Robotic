# perception/temporal_filter.py
from typing import Tuple, List
#
# Sprint 1 / S1-5 — Pure-Python 3-frame temporal confirmation filter.
# No ROS2, no OpenCV, no external dependencies.
#
# Input:  classified state integers (0=UNKNOWN, 1=RED, 2=YELLOW, 3=GREEN),
#         monotonic wall-clock milliseconds.
# Output: (accumulated_state, confirmed) after each update.
#
# Rules:
#   - confirm_frames consecutive non-UNKNOWN same-state observations → confirmed=True.
#   - Any UNKNOWN observation resets the filter immediately.
#   - A state change resets the count to 1 (starts accumulating the new state).
#   - If more than state_memory_ms elapses between updates the filter resets.
#
# Contract ref: wiki/perception/traffic_light_node.md (3-frame temporal filter)
#               wiki/contracts/message_contracts.md §8 (confirmed field semantics)

_STATE_UNKNOWN = 0


class TemporalFilter:
    """
    Temporal confirmation filter for traffic light state.

    Requires `confirm_frames` consecutive identical non-UNKNOWN classifications
    before setting confirmed=True.  Resets on UNKNOWN, state change, or when
    more than `state_memory_ms` elapses between updates.
    """

    def __init__(self, confirm_frames: int = 3, state_memory_ms: int = 500) -> None:
        if confirm_frames < 1:
            raise ValueError(f'confirm_frames must be >= 1, got {confirm_frames}')
        self._confirm_frames = confirm_frames
        self._state_memory_ms = state_memory_ms
        self._accumulated_state: int = _STATE_UNKNOWN
        self._count: int = 0
        self._last_update_ms: int = -1

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def reset(self) -> None:
        """Force-reset the filter to UNKNOWN (used on stale/missing image)."""
        self._accumulated_state = _STATE_UNKNOWN
        self._count = 0
        self._last_update_ms = -1

    def update(self, new_state: int, now_ms: int):
        """
        Feed one classified frame and return (accumulated_state, confirmed).

        Parameters
        ----------
        new_state : int
            0=UNKNOWN, 1=RED, 2=YELLOW, 3=GREEN.
            UNKNOWN immediately resets the filter.
        now_ms : int
            Monotonic wall-clock time in milliseconds for memory-expiry checks.

        Returns
        -------
        Tuple[int, bool]
            (accumulated_state, confirmed)
        """
        if new_state == _STATE_UNKNOWN:
            self.reset()
            return _STATE_UNKNOWN, False

        # Expire stale accumulated state if the gap exceeds state_memory_ms.
        if self._last_update_ms >= 0 and (now_ms - self._last_update_ms) > self._state_memory_ms:
            self.reset()

        self._last_update_ms = now_ms

        if new_state == self._accumulated_state:
            self._count += 1
        else:
            self._accumulated_state = new_state
            self._count = 1

        return self._accumulated_state, self.confirmed

    # ------------------------------------------------------------------
    # Read-only properties
    # ------------------------------------------------------------------

    @property
    def confirmed(self) -> bool:
        """True when count has reached confirm_frames for a non-UNKNOWN state."""
        return self._count >= self._confirm_frames and self._accumulated_state != _STATE_UNKNOWN

    @property
    def count(self) -> int:
        """Consecutive-frame count for the currently accumulated state."""
        return self._count

    @property
    def accumulated_state(self) -> int:
        """State currently being accumulated (may not be confirmed yet)."""
        return self._accumulated_state

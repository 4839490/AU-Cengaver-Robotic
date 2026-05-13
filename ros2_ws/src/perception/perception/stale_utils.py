# perception/stale_utils.py
#
# Pure-Python utility for resolving the effective stale threshold used by
# traffic_light_node and any other node that must not hold evidence past its
# validity window.
#
# Contract ref: wiki/contracts/timing_and_fallback.md (valid_until_ms per topic)
#               wiki/perception/traffic_light_node.md (stale semantics)


def resolve_stale_ms(configured_ms: int, valid_until_ms: int) -> int:
    """
    Return the effective stale threshold, clamped to the validity window.

    Rules
    -----
    1. If ``configured_ms <= 0`` (invalid / not set): return ``valid_until_ms``.
    2. If ``configured_ms > valid_until_ms``: return ``valid_until_ms``
       (clamp — stale threshold must never exceed message validity window).
    3. Otherwise: return ``configured_ms`` unchanged.

    The caller is responsible for logging a warning when the returned value
    differs from ``configured_ms``.

    Parameters
    ----------
    configured_ms : int
        Value read from the ROS2 parameter (or supplied by the caller).
    valid_until_ms : int
        Message validity window in ms (e.g. VALID_UNTIL_LIGHT_MS = 300).

    Returns
    -------
    int
        Effective stale threshold in ms.
    """
    if configured_ms <= 0:
        return valid_until_ms
    return min(configured_ms, valid_until_ms)

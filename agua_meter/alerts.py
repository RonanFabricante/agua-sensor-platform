"""Usage alerts for AquaSense meters."""
from datetime import time

# TODO(AGUA hero task): make the overnight leak threshold configurable per household.
OVERNIGHT_START = time(0, 0)
OVERNIGHT_END = time(5, 0)


def is_overnight(t: time) -> bool:
    return OVERNIGHT_START <= t < OVERNIGHT_END

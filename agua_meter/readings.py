"""Flow-rate reading validation for AquaSense meters."""

MIN_FLOW_L_PER_MIN = 0.0
MAX_FLOW_L_PER_MIN = 60.0


def is_valid_reading(flow_l_per_min: float) -> bool:
    """Return True if a flow reading is physically plausible for a household meter."""
    return MIN_FLOW_L_PER_MIN <= flow_l_per_min <= MAX_FLOW_L_PER_MIN

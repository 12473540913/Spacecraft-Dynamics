"""Actuator models."""

import numpy as np


def saturate_torque(command_nm: np.ndarray, max_torque_nm: float) -> np.ndarray:
    """Apply independent axis torque saturation."""
    return np.clip(np.asarray(command_nm, dtype=float), -max_torque_nm, max_torque_nm)

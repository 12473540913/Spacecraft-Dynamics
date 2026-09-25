"""Translational spacecraft dynamics."""

import numpy as np
from spacecraft_dynamics.constants import MU_EARTH


def two_body_derivative(_t: float, state: np.ndarray, mu: float = MU_EARTH) -> np.ndarray:
    """Return [velocity, acceleration] for a Cartesian two-body state."""
    r = np.asarray(state[:3], dtype=float)
    v = np.asarray(state[3:6], dtype=float)
    r_norm = np.linalg.norm(r)
    if r_norm == 0:
        raise ValueError("Position magnitude must be nonzero.")
    a = -mu * r / r_norm**3
    return np.concatenate((v, a))

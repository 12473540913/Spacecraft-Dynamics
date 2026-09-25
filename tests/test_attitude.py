import numpy as np
from spacecraft_dynamics.dynamics.attitude import normalize_quaternion


def test_normalize_quaternion():
    q = normalize_quaternion(np.array([2.0, 0.0, 0.0, 0.0]))
    assert np.isclose(np.linalg.norm(q), 1.0)

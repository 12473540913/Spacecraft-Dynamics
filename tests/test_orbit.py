import numpy as np
from spacecraft_dynamics.dynamics.orbit import two_body_derivative


def test_two_body_acceleration_points_inward():
    state = np.array([7.0e6, 0, 0, 0, 7500, 0], dtype=float)
    derivative = two_body_derivative(0.0, state)
    assert derivative[3] < 0
    assert derivative[4] == 0
    assert derivative[5] == 0

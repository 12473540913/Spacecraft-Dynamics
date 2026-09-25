"""Minimal PID controller scaffold."""

from dataclasses import dataclass
import numpy as np


@dataclass
class PIDController:
    kp: float
    ki: float
    kd: float

    def command(self, error: np.ndarray, integral: np.ndarray, error_rate: np.ndarray) -> np.ndarray:
        return self.kp * error + self.ki * integral + self.kd * error_rate

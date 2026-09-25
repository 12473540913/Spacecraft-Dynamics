"""Sensor models."""

from dataclasses import dataclass
import numpy as np


@dataclass
class GyroModel:
    noise_std_rad_s: float = 0.0
    bias_rad_s: np.ndarray | None = None

    def measure(self, omega_true: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        bias = np.zeros(3) if self.bias_rad_s is None else np.asarray(self.bias_rad_s)
        noise = rng.normal(0.0, self.noise_std_rad_s, 3)
        return np.asarray(omega_true) + bias + noise

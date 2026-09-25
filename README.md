# Spacecraft Dynamics – a GNC Digital Twin

A spacecraft Guidance, Navigation, and Control (GNC) simulation platform for studying orbital motion, attitude dynamics, sensing, estimation, actuation, feedback control, and autonomous maneuvering.

## Project goals

1. Build a modular spacecraft digital twin from first principles.
2. Connect orbital and rigid-body dynamics to realistic sensors and actuators.
3. Implement state estimation and closed-loop attitude/orbit control.
4. Quantify controller and estimator performance under disturbances and uncertainty.
5. Produce reproducible experiments, visualizations, and a publication-quality technical contribution.

## Core stack

**Software:** Python, NumPy, SciPy, pandas, Matplotlib, JupyterLab, pytest  
**Models:** orbital mechanics, rigid-body rotational dynamics, sensor/actuator models, environmental disturbances  
**Methods:** state-space modeling, numerical integration, PID/LQR control, Kalman filtering/EKF, Monte Carlo analysis

## Repository map

| Path | Purpose |
|---|---|
| `notebooks/` | Numbered investigations and demonstrations |
| `src/spacecraft_dynamics/` | Reusable simulation/GNC package |
| `configs/` | Spacecraft, orbit, sensor, actuator, and experiment parameters |
| `tests/` | Unit and regression tests |
| `data/` | Small generated/reference datasets only |
| `figures/` | Generated plots and diagrams |
| `docs/` | Theory notes and technical documentation |
| `publication/` | Essay/paper manuscript, figures, and reproducibility material |
| `examples/` | Small runnable end-to-end scenarios |

## Planned investigations

1. Two-body orbital propagation
2. Rigid-body attitude propagation
3. Reaction-wheel attitude control
4. Sensor simulation and measurement noise
5. Attitude estimation
6. Closed-loop pointing and stabilization
7. Environmental disturbances
8. Autonomous maneuver sequence
9. Monte Carlo robustness study
10. Publication experiment

## Publication direction

The final contribution should make a narrow, defensible technical claim rather than simply describe the simulator. A strong direction is a reproducible comparison of attitude-estimation/control performance under realistic sensor noise, actuator limits, model uncertainty, and external disturbances.

See `publication/OUTLINE.md`.

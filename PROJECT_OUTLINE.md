# Project Outline

## Phase 0 — Foundation
- Establish units, frames, conventions, state definitions, and configuration format.
- Implement reusable numerical utilities.
- Add automated tests before coupling subsystems.

## Phase 1 — Translational dynamics
- Two-body point-mass orbit model.
- Numerical propagation.
- Conserved-energy/angular-momentum checks.
- Ground-track/orbit visualization as an optional extension.

## Phase 2 — Rotational dynamics
- Quaternion attitude representation.
- Body angular velocity and inertia tensor.
- Euler rigid-body equations.
- Quaternion normalization and frame-convention tests.

## Phase 3 — Actuation and control
- Reaction-wheel model.
- Torque saturation and momentum limits.
- Baseline PID attitude controller.
- LQR/state-space controller extension.
- Pointing, detumble, and slew experiments.

## Phase 4 — Sensors and navigation
- Gyroscope, sun-sensor/star-tracker style measurement models.
- Bias, white noise, sample rate, dropout.
- Attitude estimator.
- EKF extension and covariance tracking.
- Truth-versus-estimate error metrics.

## Phase 5 — Environment and uncertainty
- Gravity-gradient torque.
- Simple aerodynamic and solar-radiation-pressure disturbances.
- Parameter uncertainty.
- Monte Carlo campaigns.

## Phase 6 — Integrated digital twin
- Couple orbit, attitude, sensors, estimator, controller, actuators, and disturbances.
- Build scenario runner from YAML configuration.
- Log truth, measurements, estimates, commands, and actuator states.
- Create interactive or animated visualization layer.

## Phase 7 — Validation
- Analytical sanity checks.
- Conservation tests for unforced dynamics.
- Unit tests for frames/quaternions.
- Regression scenarios.
- Compare selected results with textbook/reference cases.

## Phase 8 — Publication contribution
- Choose one narrow research question.
- Define hypothesis and metrics before running final experiments.
- Run deterministic and Monte Carlo experiments.
- Report uncertainty and limitations.
- Produce manuscript/essay plus fully reproducible code/configs/results.

## Suggested publication question
**How do estimator design and actuator constraints interact to determine spacecraft pointing performance under realistic sensor noise and external disturbances?**

Possible comparison:
- complementary/baseline estimator vs EKF
- PID vs LQR
- nominal vs noisy/biased sensors
- unconstrained vs saturated reaction wheels
- nominal vs disturbed dynamics

Primary metrics:
- RMS pointing error
- settling time
- control effort
- estimator error
- wheel momentum/saturation frequency
- failure/recovery rate across Monte Carlo trials

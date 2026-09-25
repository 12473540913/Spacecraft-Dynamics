# Validation Strategy

Every model should have at least one independent check.

## Orbit
- Circular-orbit period check
- Specific orbital energy conservation
- Angular momentum conservation

## Attitude
- Quaternion norm remains approximately 1
- Torque-free angular momentum/energy checks
- Known constant-axis rotation case

## Estimation
- Zero-noise convergence
- Innovation/residual inspection
- Covariance consistency checks

## Control
- Step/slew response
- Settling time and overshoot
- Saturation behavior
- Disturbance rejection

## Integrated simulation
- Fixed seeded regression case
- Monte Carlo statistics
- Numerical-step sensitivity

# AquaSense Sensor Platform

Backend services for the AquaSense smart water meter used by Agua Inc. consumer and business customers.

## Modules
- `agua_meter/alerts.py` — usage alerts (leak detection, abnormal flow)
- `agua_meter/readings.py` — flow-rate reading validation

## Working with ClickUp
Every branch, commit and PR must reference a ClickUp task ID, e.g. `AGUA-12`.
Branches are created from ClickUp (`feature/AGUA-12-task-name`) so they link automatically.
Move status from a commit by adding it in brackets: `AGUA-12[in review] add threshold config`.

## Run tests
```
python -m pytest
```
Test
Dry run
Dry run AGUA-6
edited for fix

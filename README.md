# Employee Leave Management

A small Python application for validating employee leave requests against an employee's available leave balance.

## Validate a leave request

`request_leave` returns a `LeaveRequest` with the remaining balance, or raises
`ValueError` when the employee name, requested days, or available balance is
invalid or the request exceeds the balance.

Run the sample leave-balance validation:

```sh
python -m scripts.validate_leave_balance
```

Run the automated pytest suite (including the existing unit tests):

```sh
python -m pip install pytest
python -m pytest -v
```

## Run in Docker

Build and run the validation container:

```sh
docker build -t employee-leave-management .
docker run --rm employee-leave-management
```

## Continuous integration

The GitHub Actions workflow at `.github/workflows/validate-leave-balance.yml`
runs pytest and the leave-balance validation module whenever changes are pushed
to `main`.

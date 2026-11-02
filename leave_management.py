"""Leave request validation for the employee leave management application."""

from dataclasses import dataclass


@dataclass(frozen=True)
class LeaveRequest:
    employee_name: str
    requested_days: int
    remaining_balance: int


def request_leave(
    employee_name: str, requested_days: int, available_days: int
) -> LeaveRequest:
    """Validate a leave request and return its resulting balance."""
    if not isinstance(employee_name, str) or not employee_name.strip():
        raise ValueError("Employee name must not be empty.")
    if (
        isinstance(requested_days, bool)
        or not isinstance(requested_days, int)
        or requested_days <= 0
    ):
        raise ValueError("Requested leave days must be a positive integer.")
    if (
        isinstance(available_days, bool)
        or not isinstance(available_days, int)
        or available_days < 0
    ):
        raise ValueError("Available leave balance must be a non-negative integer.")
    if requested_days > available_days:
        raise ValueError(
            f"Insufficient leave balance for {employee_name.strip()}: "
            f"requested {requested_days} day(s), "
            f"but only {available_days} day(s) are available."
        )

    return LeaveRequest(
        employee_name=employee_name.strip(),
        requested_days=requested_days,
        remaining_balance=available_days - requested_days,
    )

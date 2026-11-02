import pytest

from leave_management import request_leave


@pytest.mark.parametrize(
    ("requested_days", "available_days", "expected_remaining", "expected_error"),
    [
        pytest.param(4, 10, 6, None, id="valid-request"),
        pytest.param(11, 10, None, "Insufficient leave balance", id="insufficient-balance"),
        pytest.param(0, 10, None, "positive integer", id="zero-days"),
        pytest.param(-1, 10, None, "positive integer", id="invalid-negative-days"),
    ],
)
def test_request_leave(
    requested_days: int,
    available_days: int,
    expected_remaining: int | None,
    expected_error: str | None,
) -> None:
    if expected_error is not None:
        with pytest.raises(ValueError, match=expected_error):
            request_leave("Taylor Morgan", requested_days, available_days)
        return

    result = request_leave("Taylor Morgan", requested_days, available_days)

    assert result.employee_name == "Taylor Morgan"
    assert result.requested_days == requested_days
    assert result.remaining_balance == expected_remaining

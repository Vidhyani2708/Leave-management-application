import pytest

from leave_management import request_leave


@pytest.mark.parametrize(
    ("requested_days", "available_days", "expected"),
    [
        (4, 10, 6),
        (11, 10, "Insufficient leave balance"),
        (0, 10, "positive integer"),
        (-1, 10, "positive integer"),
    ],
)
def test_request_leave(requested_days, available_days, expected):
    if isinstance(expected, str):
        with pytest.raises(ValueError, match=expected):
            request_leave("Taylor Morgan", requested_days, available_days)
    else:
        assert (
            request_leave("Taylor Morgan", requested_days, available_days).remaining_balance
            == expected
        )

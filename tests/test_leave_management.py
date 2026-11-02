import unittest

from leave_management import LeaveRequest, request_leave


class RequestLeaveTests(unittest.TestCase):
    def test_approves_request_and_calculates_remaining_balance(self) -> None:
        result = request_leave(" Avery Chen ", 5, 20)

        self.assertEqual(result, LeaveRequest("Avery Chen", 5, 15))

    def test_allows_request_for_exact_available_balance(self) -> None:
        result = request_leave("Jordan Patel", 3, 3)

        self.assertEqual(result.remaining_balance, 0)

    def test_rejects_request_exceeding_available_balance(self) -> None:
        with self.assertRaisesRegex(ValueError, "Insufficient leave balance"):
            request_leave("Avery Chen", 6, 5)

    def test_rejects_non_positive_requested_days(self) -> None:
        for days in (0, -1, True):
            with self.subTest(days=days), self.assertRaises(ValueError):
                request_leave("Avery Chen", days, 5)

    def test_rejects_invalid_available_balance(self) -> None:
        for balance in (-1, True):
            with self.subTest(balance=balance), self.assertRaises(ValueError):
                request_leave("Avery Chen", 1, balance)

    def test_rejects_empty_employee_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "Employee name"):
            request_leave("  ", 1, 5)


if __name__ == "__main__":
    unittest.main()

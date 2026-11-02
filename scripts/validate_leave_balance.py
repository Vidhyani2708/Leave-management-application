"""Validate the sample leave requests stored in data/leave_requests.json."""

import json
import sys
from pathlib import Path

from leave_management import request_leave


def main() -> int:
    requests_path = Path(__file__).resolve().parents[1] / "data" / "leave_requests.json"

    try:
        with requests_path.open(encoding="utf-8") as requests_file:
            requests = json.load(requests_file)

        if not isinstance(requests, list):
            raise ValueError("The leave requests file must contain a JSON array.")

        for index, request in enumerate(requests, start=1):
            if not isinstance(request, dict):
                raise ValueError(f"Leave request {index} must be a JSON object.")
            request_leave(
                request["employee_name"],
                request["requested_days"],
                request["available_days"],
            )
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Leave balance validation failed: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(requests)} leave request(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

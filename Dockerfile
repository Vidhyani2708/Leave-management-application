FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY leave_management.py .
COPY scripts/ scripts/
COPY data/ data/

USER 10001:10001

CMD ["python", "-m", "scripts.validate_leave_balance"]

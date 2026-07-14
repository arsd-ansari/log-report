import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_exists():
    """Criterion 1: /app/report.json exists."""
    assert REPORT.exists(), "report.json not found"


def test_total_requests():
    """Criterion 2: total_requests equals 6 (total log lines)."""
    data = json.loads(REPORT.read_text())
    assert data["total_requests"] == 6, f"expected 6, got {data.get('total_requests')}"


def test_unique_ips():
    """Criterion 3: unique_ips equals 3 (distinct client IP addresses)."""
    data = json.loads(REPORT.read_text())
    assert data["unique_ips"] == 3, f"expected 3, got {data.get('unique_ips')}"


def test_top_path():
    """Criterion 4: top_path equals /index.html (most-requested path)."""
    data = json.loads(REPORT.read_text())
    assert data["top_path"] == "/index.html", f"expected /index.html, got {data.get('top_path')}"

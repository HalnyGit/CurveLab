from datetime import date

from curvelab.core.dates import date_to_internal_date, internal_date_to_date
from curvelab.core.dates import add_months


def test_epoch_date():
    # Test that the epoch date (2000-01-01) converts to 0
    assert date_to_internal_date(date(2000, 1, 1)) == 0


def test_day_after_epoch():
    # Test that the day after the epoch (2000-01-02) converts to 1
    assert date_to_internal_date(date(2000, 1, 2)) == 1


def test_day_before_epoch():
    # Test that the day before the epoch (1999-12-31) converts to -1
    assert date_to_internal_date(date(1999, 12, 31)) == -1


def test_round_trip():
    # Test that converting a date to internal and back gives the original date
    original_date = date(2026, 5, 30)
    internal_date = date_to_internal_date(original_date)
    converted_date = internal_date_to_date(internal_date)
    assert converted_date == original_date


def test_add_months_regular_date():
    assert add_months(date(2026, 1, 15), 1) == date(2026, 2, 15)


def test_add_months_end_of_month_to_shorter_month():
    assert add_months(date(2026, 1, 31), 1) == date(2026, 2, 28)


def test_add_months_across_year_end():
    assert add_months(date(2026, 11, 30), 3) == date(2027, 2, 28)


def test_add_months_leap_year_february():
    assert add_months(date(2024, 1, 31), 1) == date(2024, 2, 29)

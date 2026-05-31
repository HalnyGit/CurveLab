from datetime import date

from curvelab.core.dates import date_to_internal_date

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
    assert internal_date == (original_date - date(2000, 1, 1)).days

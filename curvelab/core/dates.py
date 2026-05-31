from datetime import date, timedelta

# CurveLab Internal Date:
# Internal Date = Calendar Date - EPOCH
# Measured as calendar days since 2000-01-01
EPOCH = date(2000, 1, 1)

def date_to_internal_date(d: date) -> int:
    """
    Convert a calendar date to a CurveLab Internal Date.
    Internal Date = number of calendar days since EPOCH.
    """
    return (d - EPOCH).days

def internal_date_to_date(internal_date: int) -> date:
    """
    Convert a CurveLab Internal Date back to a calendar date.
    Calendar Date = EPOCH + Internal Date (in days).
    """
    return EPOCH + timedelta(days=internal_date)






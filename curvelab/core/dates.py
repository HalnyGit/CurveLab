import calendar
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


def days_in_year(year: int) -> int:
    return 366 if is_leap_year(year) else 365


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def add_months(d: date, months: int) -> date:
    """
    Add calendar months to a date.

    If the original day does not exist in the target month,
    use the last day of the target month.
    """
    target_month = d.month + months
    target_year = d.year + (target_month - 1) // 12
    target_month = (target_month - 1) % 12 + 1

    last_day = calendar.monthrange(target_year, target_month)[1]
    target_day = min(d.day, last_day)

    return date(target_year, target_month, target_day)




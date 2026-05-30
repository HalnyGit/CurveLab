from datetime import date

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






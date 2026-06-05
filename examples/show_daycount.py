from datetime import date

from curvelab.core.dates import date_to_internal_date
from curvelab.core.daycount import ActActISDA

start = date_to_internal_date(date(2023, 7, 1))
end = date_to_internal_date(date(2024, 7, 1))

dc = ActActISDA()

print(dc.year_fraction(start, end))

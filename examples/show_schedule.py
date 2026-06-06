from datetime import date

from curvelab.core.dates import date_to_internal_date, internal_date_to_date
from curvelab.core.schedule import Frequency, ScheduleBuilder


start = date_to_internal_date(date(2026, 1, 1))
end = date_to_internal_date(date(2027, 1, 1))

schedule = ScheduleBuilder().build(
    start_date=start,
    end_date=end,
    frequency=Frequency(months=3),
)

for i, period in enumerate(schedule.periods, start=1):
    print(
        i,
        internal_date_to_date(period.calculation_start_date),
        "->",
        internal_date_to_date(period.calculation_end_date),
        "pay",
        internal_date_to_date(period.payment_date),
        "fix",
        period.fixing_date
    )

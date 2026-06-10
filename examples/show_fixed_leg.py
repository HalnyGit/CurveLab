from datetime import date

from curvelab.core.dates import (
    date_to_internal_date,
    internal_date_to_date,
)
from curvelab.core.daycount import Act365
from curvelab.core.schedule import Frequency, ScheduleBuilder
from curvelab.instruments.fixed_leg import FixedLeg


start = date_to_internal_date(date(2026, 1, 1))
end = date_to_internal_date(date(2027, 1, 1))

schedule = ScheduleBuilder().build(
    start_date=start,
    end_date=end,
    frequency=Frequency(months=3),
)

leg = FixedLeg(
    schedule=schedule,
    notional=100_000_000,
    fixed_rate=0.05,
    currency="PLN",
    day_count=Act365(),
)

cashflows = leg.generate_cashflows()

for i, cashflow in enumerate(cashflows, start=1):
    print(
        i,
        internal_date_to_date(cashflow.payment_date),
        cashflow.currency,
        round(cashflow.amount, 2),
    )

from datetime import date

from curvelab.core.dates import (
    date_to_internal_date,
    internal_date_to_date,
)
from curvelab.core.daycount import Act365
from curvelab.core.schedule import Frequency, ScheduleBuilder

from curvelab.instruments.index import IborIndex
from curvelab.instruments.floating_leg import FloatingLeg


start = date_to_internal_date(date(2026, 1, 1))
end = date_to_internal_date(date(2027, 1, 1))

schedule = ScheduleBuilder().build(
    start_date=start,
    end_date=end,
    frequency=Frequency(months=3),
)

index = IborIndex(
    name="WIBOR3M",
    currency="PLN",
    tenor_months=3,
    fixing_lag_days=2,
)

leg = FloatingLeg(
    schedule=schedule,
    notional=100_000_000,
    currency="PLN",
    index=index,
    spread=0.0025,
    day_count=Act365(),
    forward_rate=0.05,
)

cashflows = leg.generate_cashflows()

print(f"Index: {index.name}")
print()

for i, cashflow in enumerate(cashflows, start=1):
    print(
        i,
        internal_date_to_date(cashflow.payment_date),
        cashflow.currency,
        round(cashflow.amount, 2),
    )

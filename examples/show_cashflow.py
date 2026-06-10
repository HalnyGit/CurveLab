from datetime import date

from curvelab.core.dates import date_to_internal_date, internal_date_to_date
from curvelab.instruments.cashflow import Cashflow


cf = Cashflow(
    payment_date=date_to_internal_date(date(2026, 4, 1)),
    currency="PLN",
    amount=125_000.0,
)

print("Payment date:", internal_date_to_date(cf.payment_date))
print("Currency    :", cf.currency)
print("Amount      :", cf.amount)

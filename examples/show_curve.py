from datetime import date

from curvelab.core.dates import (
    date_to_internal_date,
    internal_date_to_date,
)
from curvelab.curves.curve import DiscountCurve


curve = DiscountCurve(
    curve_name="PLN_WIBOR3M",
    valuation_date=date_to_internal_date(date(2026, 1, 1)),
    points=[
        (date_to_internal_date(date(2026, 4, 1)), 0.987821),
        (date_to_internal_date(date(2026, 7, 1)), 0.971263),
    ],
)

print(curve.curve_name)
print()

for point_date, value in curve.points:
    print(internal_date_to_date(point_date), value)

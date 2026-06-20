from datetime import date

from curvelab.core.dates import (
    date_to_internal_date,
    internal_date_to_date,
)
from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet


valuation_date = date_to_internal_date(date(2026, 1, 1))

wibor3m_curve = Curve(
    curve_name="PLN_WIBOR3M",
    valuation_date=valuation_date,
    points=[
        (date_to_internal_date(date(2026, 4, 1)), 0.987821),
        (date_to_internal_date(date(2026, 7, 1)), 0.971263),
    ],
)

lch_discount_curve = Curve(
    curve_name="PLN_LCH_DISCOUNT",
    valuation_date=valuation_date,
    points=[
        (date_to_internal_date(date(2026, 4, 1)), 0.988000),
        (date_to_internal_date(date(2026, 7, 1)), 0.972000),
    ],
)

curve_set = CurveSet(
    curves={
        "PLN_WIBOR3M": wibor3m_curve,
        "PLN_LCH_DISCOUNT": lch_discount_curve,
    }
)

print("CurveSet")
print()

for curve_name, curve in curve_set.curves.items():
    print(curve_name)

    for point_date, df in curve.points:
        print(" ", internal_date_to_date(point_date), df)

    print()

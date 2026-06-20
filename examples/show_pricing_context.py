from datetime import date

from curvelab.core.dates import date_to_internal_date
from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet
from curvelab.pricing.pricing_context import PricingContext


valuation_date = date_to_internal_date(date(2026, 1, 1))

wibor3m_curve = Curve(
    curve_name="PLN_WIBOR3M",
    valuation_date=valuation_date,
    points=[
        (date_to_internal_date(date(2026, 1, 1)), 1.0),
        (date_to_internal_date(date(2026, 4, 1)), 0.987821),
    ],
)

curve_set = CurveSet(
    curves={
        "PLN_WIBOR3M": wibor3m_curve,
    }
)

context = PricingContext(
    curve_set=curve_set,
    curve_map={
        "WIBOR3M": "PLN_WIBOR3M",
        "PLN_DEPO": "PLN_WIBOR3M",
    },
)

curve = context.get_curve("WIBOR3M")

print("PricingContext")
print()
print("WIBOR3M maps to:", curve.curve_name)
print("DF 2026-04-01:", curve.get_df(date_to_internal_date(date(2026, 4, 1))))

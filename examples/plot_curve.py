from datetime import date

import matplotlib.pyplot as plt

from curvelab.core.dates import (
    date_to_internal_date,
    internal_date_to_date,
)
from curvelab.curves.curve import Curve


curve = Curve(
    curve_name="PLN_WIBOR3M",
    valuation_date=date_to_internal_date(date(2026, 1, 1)),
    points=[
        (date_to_internal_date(date(2026, 4, 1)), 0.987821),
        (date_to_internal_date(date(2026, 7, 1)), 0.971263),
    ],
)

dates = [
    internal_date_to_date(point_date)
    for point_date, _ in curve.points
]

values = [
    value
    for _, value in curve.points
]

plt.plot(dates, values, marker="o")
plt.title(curve.curve_name)
plt.xlabel("Date")
plt.ylabel("Discount factor")
plt.grid(True)
plt.show()

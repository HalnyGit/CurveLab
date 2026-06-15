import pytest

from curvelab.curves.curve import DiscountCurve


def test_discount_curve_exact_date_lookup():
    curve = DiscountCurve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[
            (365, 0.95),
        ],
    )

    assert curve.discount_factor(365) == pytest.approx(0.95)


def test_discount_curve_missing_date_raises_error():
    curve = DiscountCurve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[],
    )

    with pytest.raises(KeyError):
        curve.discount_factor(365)

import pytest

from curvelab.curves.curve import Curve


def test_discount_curve_exact_date_lookup():
    curve = Curve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[
            (365, 0.95),
        ],
    )

    assert curve.get_df(365) == pytest.approx(0.95)


def test_discount_curve_missing_date_raises_error():
    curve = Curve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[],
    )

    with pytest.raises(KeyError):
        curve.get_df(365)

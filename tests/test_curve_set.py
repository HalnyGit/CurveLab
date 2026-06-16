import pytest

from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet


def test_curve_set_returns_curve():
    curve = Curve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[
            (365, 0.95),
        ],
    )

    curve_set = CurveSet(
        curves={
            "PLN_WIBOR3M": curve,
        }
    )

    assert curve_set.get("PLN_WIBOR3M") == curve


def test_curve_set_raises_for_missing_curve():
    curve_set = CurveSet(
        curves={}
    )

    with pytest.raises(KeyError):
        curve_set.get("PLN_WIBOR3M")

import pytest

from curvelab.core.daycount import Act365
from curvelab.instruments.fra import FRA
from curvelab.instruments.index import IborIndex
from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet
from curvelab.pricing.pricing_context import PricingContext


def make_wibor3m() -> IborIndex:
    return IborIndex(
        name="WIBOR3M",
        currency="PLN",
        tenor_months=3,
        fixing_lag_days=2,
    )


def test_fra_fixed_and_floating_interest():
    fra = FRA(
        side="pay_fixed",
        start_date=0,
        end_date=365,
        notional=100.0,
        fixed_rate=0.05,
        forward_rate=0.06,
        currency="PLN",
        index=make_wibor3m(),
        day_count=Act365(),
    )

    assert fra.tau == pytest.approx(1.0)
    assert fra.fixed_leg_interest() == pytest.approx(5.0)
    assert fra.floating_leg_interest() == pytest.approx(6.0)


def test_fra_pay_fixed_settlement_positive_when_forward_above_fixed():
    fra = FRA(
        side="pay_fixed",
        start_date=0,
        end_date=365,
        notional=100.0,
        fixed_rate=0.05,
        forward_rate=0.06,
        currency="PLN",
        index=make_wibor3m(),
        day_count=Act365(),
    )

    expected = 100.0 * (0.06 - 0.05) * 1.0 / (1 + 0.06 * 1.0)

    cashflows = fra.generate_cashflows()

    assert len(cashflows) == 1
    assert cashflows[0].payment_date == 0
    assert cashflows[0].currency == "PLN"
    assert cashflows[0].amount == pytest.approx(expected)


def test_fra_receive_fixed_settlement_negative_when_forward_above_fixed():
    fra = FRA(
        side="receive_fixed",
        start_date=0,
        end_date=365,
        notional=100.0,
        fixed_rate=0.05,
        forward_rate=0.06,
        currency="PLN",
        index=make_wibor3m(),
        day_count=Act365(),
    )

    expected = -100.0 * (0.06 - 0.05) * 1.0 / (1 + 0.06 * 1.0)

    cashflows = fra.generate_cashflows()

    assert cashflows[0].amount == pytest.approx(expected)


def test_fra_invalid_side_raises_error():
    fra = FRA(
        side="wrong",
        start_date=0,
        end_date=365,
        notional=100.0,
        fixed_rate=0.05,
        forward_rate=0.06,
        currency="PLN",
        index=make_wibor3m(),
        day_count=Act365(),
    )

    with pytest.raises(ValueError):
        fra.generate_cashflows()

def test_fra_get_rate_from_curve_set():
    curve = Curve(
        curve_name="PLN_WIBOR3M",
        valuation_date=0,
        points=[
            (0, 1.0),
            (365, 0.95),
        ],
    )

    curve_set = CurveSet(
        curves={
        "PLN_WIBOR3M": curve,
        },
    )

    context = PricingContext(
        curve_set=curve_set,
        curve_map={
            "WIBOR3M": "PLN_WIBOR3M",
        },
    )

    fra = FRA(
        side="pay_fixed",
        start_date=0,
        end_date=365,
        notional=100.0,
        fixed_rate=0.05,
        forward_rate=0.06,
        currency="PLN",
        index=make_wibor3m(),
        day_count=Act365(),
    )

    expected_rate = ((1.0 / 0.95) - 1.0) / 1.0

    assert fra.get_rate(context) == pytest.approx(expected_rate)

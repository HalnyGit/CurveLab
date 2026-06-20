import pytest

from curvelab.core.daycount import Act365
from curvelab.instruments.deposit import Deposit
from curvelab.curves.curve import Curve
from curvelab.curves.curve_set import CurveSet
from curvelab.pricing.pricing_context import PricingContext


def test_lend_deposit_generates_cashflows():
    deposit = Deposit(
        side="lend",
        start_date=0,
        end_date=365,
        notional=100.0,
        rate=0.05,
        currency="PLN",
        day_count=Act365(),
        curve_key="PLN_DEPO"
    )

    cashflows = deposit.generate_cashflows()

    assert len(cashflows) == 2

    assert cashflows[0].payment_date == 0
    assert cashflows[0].currency == "PLN"
    assert cashflows[0].amount == pytest.approx(-100.0)

    assert cashflows[1].payment_date == 365
    assert cashflows[1].currency == "PLN"
    assert cashflows[1].amount == pytest.approx(105.0)


def test_borrow_deposit_generates_cashflows():
    deposit = Deposit(
        side="borrow",
        start_date=0,
        end_date=365,
        notional=100.0,
        rate=0.05,
        currency="PLN",
        day_count=Act365(),
        curve_key="PLN_DEPO"
    )

    cashflows = deposit.generate_cashflows()

    assert len(cashflows) == 2

    assert cashflows[0].amount == pytest.approx(100.0)
    assert cashflows[1].amount == pytest.approx(-105.0)


def test_deposit_invalid_side_raises_error():
    deposit = Deposit(
        side="wrong",
        start_date=0,
        end_date=365,
        notional=100.0,
        rate=0.05,
        currency="PLN",
        day_count=Act365(),
        curve_key="PLN_DEPO"
    )

    with pytest.raises(ValueError):
        deposit.generate_cashflows()


def test_deposit_get_rate_from_pricing_context():
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
        }
    )

    context = PricingContext(
        curve_set=curve_set,
        curve_map={
            "PLN_DEPO": "PLN_WIBOR3M",
        },
    )

    deposit = Deposit(
        side="lend",
        start_date=0,
        end_date=365,
        notional=100.0,
        rate=0.05,
        currency="PLN",
        day_count=Act365(),
        curve_key="PLN_DEPO",
    )

    expected_rate = ((1.0 / 0.95) - 1.0) / 1.0

    assert deposit.get_rate(context) == pytest.approx(expected_rate)
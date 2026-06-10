import pytest

from curvelab.core.daycount import Act365
from curvelab.instruments.deposit import Deposit


def test_lend_deposit_generates_cashflows():
    deposit = Deposit(
        side="lend",
        start_date=0,
        end_date=365,
        notional=100.0,
        rate=0.05,
        currency="PLN",
        day_count=Act365(),
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
    )

    with pytest.raises(ValueError):
        deposit.generate_cashflows()
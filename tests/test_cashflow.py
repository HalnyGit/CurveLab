from curvelab.instruments.cashflow import Cashflow


def test_cashflow_creation():

    cf = Cashflow(
        payment_date=1000,
        currency="PLN",
        amount=125000.0,
    )

    assert cf.payment_date == 1000
    assert cf.currency == "PLN"
    assert cf.amount == 125000.0

import pytest

from curvelab.core.daycount import Act365
from curvelab.core.schedule import Period, Schedule
from curvelab.instruments.floating_leg import FloatingLeg
from curvelab.instruments.index import IborIndex


def test_floating_leg_generates_cashflows():
    schedule = Schedule(
        periods=[
            Period(
                calculation_start_date=0,
                calculation_end_date=365,
                payment_date=365,
            )
        ]
    )

    index = IborIndex(
        name="WIBOR_3M",
        currency="PLN",
        tenor_months=3,
        fixing_lag_days=2,
    )

    leg = FloatingLeg(
        schedule=schedule,
        notional=100.0,
        currency="PLN",
        index=index,
        spread=0.0025,
        day_count=Act365(),
        forward_rate=0.05,
    )

    cashflows = leg.generate_cashflows()

    assert len(cashflows) == 1
    assert cashflows[0].amount == pytest.approx(5.25)
    assert cashflows[0].currency == "PLN"
    assert cashflows[0].payment_date == 365

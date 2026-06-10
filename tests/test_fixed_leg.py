from curvelab.core.daycount import Act365
from curvelab.core.schedule import Period, Schedule
from curvelab.instruments.fixed_leg import FixedLeg


def test_fixed_leg_generates_cashflows():
    schedule = Schedule(
        periods=[
            Period(
                calculation_start_date=0,
                calculation_end_date=365,
                payment_date=365,
            )
        ]
    )

    leg = FixedLeg(
        schedule=schedule,
        notional=100.0,
        fixed_rate=0.05,
        currency="PLN",
        day_count=Act365(),
    )

    cashflows = leg.generate_cashflows()

    assert len(cashflows) == 1
    assert cashflows[0].amount == 5.0
    assert cashflows[0].currency == "PLN"
    assert cashflows[0].payment_date == 365

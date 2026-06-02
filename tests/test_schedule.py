from curvelab.core.schedule import Schedule, Period

def test_schedule_contains_periods():
    p1 = Period(
        calculation_start_date=0,
        calculation_end_date=90,
        payment_date=90,
        )
    p2 = Period(
        calculation_start_date=90,
        calculation_end_date=180,
        payment_date=180,
        )

    schedule = Schedule(periods=[p1, p2])

    assert len(schedule.periods) == 2
    assert schedule.periods[0] == p1
    assert schedule.periods[1] == p2

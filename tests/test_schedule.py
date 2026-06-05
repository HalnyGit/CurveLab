from datetime import date

from curvelab.core.dates import date_to_internal_date
from curvelab.core.schedule import Frequency, Period, Schedule, ScheduleBuilder

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


def test_schedule_builder_quarterly_one_year():
    start = date_to_internal_date(date(2026, 1, 1))
    end = date_to_internal_date(date(2027, 1, 1))

    schedule = ScheduleBuilder().build(
        start_date=start,
        end_date=end,
        frequency=Frequency(months=3),
    )

    assert len(schedule.periods) == 4
    assert schedule.periods[0].calculation_start_date == start
    assert schedule.periods[-1].calculation_end_date == end
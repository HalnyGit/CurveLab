from dataclasses import dataclass

from curvelab.core.dates import (
    internal_date_to_date,
    date_to_internal_date,
    add_months,
)


@dataclass(frozen=True)
class Frequency:
    months: int


@dataclass(frozen=True)
class Period:
    """
    Represents a single accrual period within a schedule.
    """
    calculation_start_date: int
    calculation_end_date: int
    payment_date: int
    fixing_date: int | None=None
    fixing_start_date: int | None=None
    fixing_end_date: int | None=None


@dataclass(frozen=True)
class Schedule:
    """
    Represents a schedule of accrual periods.
    """
    periods: list[Period]


class ScheduleBuilder:
    """
    Builds simple regular schedules.

    MVP version:
    - no calendars
    - no business day adjustment
    - no stubs
    - payment_date = calculation_end_date
    """

    def build(
        self,
        start_date: int,
        end_date: int,
        frequency: Frequency,
    ) -> Schedule:
        if start_date >= end_date:
            raise ValueError("start_date must be before end_date")

        periods: list[Period] = []

        current_start = start_date

        while current_start < end_date:
            current_start_date = internal_date_to_date(current_start)
            next_end_date = add_months(current_start_date, frequency.months)
            current_end = date_to_internal_date(next_end_date)

            if current_end > end_date:
                current_end = end_date

            period = Period(
                calculation_start_date=current_start,
                calculation_end_date=current_end,
                payment_date=current_end,
            )

            periods.append(period)
            current_start = current_end

        return Schedule(periods=periods)





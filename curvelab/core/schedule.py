from dataclasses import dataclass


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




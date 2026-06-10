from dataclasses import dataclass

from curvelab.core.daycount import DayCount
from curvelab.core.schedule import Schedule
from curvelab.instruments.cashflow import Cashflow


@dataclass(frozen=True)
class FixedLeg:
    """
    Fixed-rate leg.

    Generates fixed-rate cashflows from a schedule.
    """

    schedule: Schedule
    notional: float
    fixed_rate: float
    currency: str
    day_count: DayCount

    def generate_cashflows(self) -> list[Cashflow]:
        cashflows: list[Cashflow] = []

        for period in self.schedule.periods:
            year_fraction = self.day_count.year_fraction(
                period.calculation_start_date,
                period.calculation_end_date,
            )

            amount = self.notional * self.fixed_rate * year_fraction

            cashflows.append(
                Cashflow(
                    payment_date=period.payment_date,
                    currency=self.currency,
                    amount=amount,
                )
            )

        return cashflows

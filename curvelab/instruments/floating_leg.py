from dataclasses import dataclass

from curvelab.core.daycount import DayCount
from curvelab.core.schedule import Schedule
from curvelab.instruments.cashflow import Cashflow
from curvelab.instruments.index import IborIndex


@dataclass(frozen=True)
class FloatingLeg:
    """
    Floating-rate leg.

    MVP version:
    - IBOR-style index
    - flat forward rate supplied directly
    - no forecast curve yet
    """

    schedule: Schedule
    notional: float
    currency: str
    index: IborIndex
    spread: float
    day_count: DayCount
    forward_rate: float

    def generate_cashflows(self) -> list[Cashflow]:
        cashflows: list[Cashflow] = []

        for period in self.schedule.periods:
            year_fraction = self.day_count.year_fraction(
                period.calculation_start_date,
                period.calculation_end_date,
            )

            amount = (
                self.notional
                * (self.forward_rate + self.spread)
                * year_fraction
            )

            cashflows.append(
                Cashflow(
                    payment_date=period.payment_date,
                    currency=self.currency,
                    amount=amount,
                )
            )

        return cashflows
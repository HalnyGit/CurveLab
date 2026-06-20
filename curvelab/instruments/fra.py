from dataclasses import dataclass

from curvelab.core.daycount import DayCount
from curvelab.instruments.cashflow import Cashflow
from curvelab.instruments.index import IborIndex
from curvelab.curves.curve_set import CurveSet
from curvelab.pricing.pricing_context import PricingContext


@dataclass(frozen=True)
class FRA:
    """
    Forward Rate Agreement.

    MVP version:
    - IBOR-style index
    - flat forward rate supplied directly
    - single settlement cashflow
    """

    side: str  # "pay_fixed" or "receive_fixed"
    start_date: int
    end_date: int
    notional: float
    fixed_rate: float
    forward_rate: float
    currency: str
    index: IborIndex
    day_count: DayCount

    @property
    def tau(self) -> float:
        return self.day_count.year_fraction(self.start_date, self.end_date)

    def fixed_leg_interest(self) -> float:
        return self.notional * self.fixed_rate * self.tau


    def floating_leg_interest(self) -> float:
        return self.notional * self.forward_rate * self.tau


    def settlement_amount(self) -> float:

        amount = (
            self.notional
            * (self.forward_rate - self.fixed_rate)
            * self.tau
            / (1 + self.forward_rate * self.tau)
        )

        if self.side == "receive_fixed":
            amount = -amount

        return amount

    def generate_cashflows(self) -> list[Cashflow]:
        if self.side not in ("pay_fixed", "receive_fixed"):
            raise ValueError("side must be 'pay_fixed' or 'receive_fixed'")

        return [
            Cashflow(
                payment_date=self.start_date,
                currency=self.currency,
                amount=self.settlement_amount(),
            )
        ]

    def get_rate(self, pricing_context: PricingContext) -> float:
        curve = pricing_context.get_curve(self.index.name)

        df_start = curve.get_df(self.start_date)
        df_end = curve.get_df(self.end_date)

        return ((df_start / df_end) - 1.0) / self.tau
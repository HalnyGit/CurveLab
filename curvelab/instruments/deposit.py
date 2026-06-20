from dataclasses import dataclass

from curvelab.core.daycount import DayCount
from curvelab.instruments.cashflow import Cashflow
from curvelab.curves.curve_set import CurveSet
from curvelab.pricing.pricing_context import PricingContext


@dataclass(frozen=True)
class Deposit:
    """
    Simple money market deposit.

    Generates initial and final cashflows.
    """
    start_date: int
    end_date: int
    notional: float
    rate: float
    currency: str
    day_count: DayCount
    curve_key: str
    side: str = "lend" # "lend" or "borrow"

    def generate_cashflows(self) -> list[Cashflow]:
        if self.side not in ("lend", "borrow"):
            raise ValueError("side must be 'lend' or 'borrow'")

        sign = -1 if self.side == "lend" else 1

        year_fraction = self.day_count.year_fraction(
            self.start_date,
            self.end_date,
        )

        start_amount = sign * self.notional
        interest = self.notional * self.rate * year_fraction
        end_amount = -sign * (self.notional + interest)

        return [
            Cashflow(
                payment_date=self.start_date,
                currency=self.currency,
                amount=start_amount,
            ),
            Cashflow(
                payment_date=self.end_date,
                currency=self.currency,
                amount=end_amount,
            ),
        ]

    def get_rate(self, pricing_context: PricingContext) -> float:
        curve = pricing_context.get_curve(self.curve_key)

        df_start = curve.get_df(self.start_date)
        df_end = curve.get_df(self.end_date)

        tau = self.day_count.year_fraction(
            self.start_date,
            self.end_date,
        )

        return ((df_start / df_end) - 1.0) / tau

from dataclasses import dataclass


@dataclass(frozen=True)
class Cashflow:
    """
    Atomic payment object in CurveLab.
    """

    payment_date: int
    currency: str
    amount: float

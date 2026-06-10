from dataclasses import dataclass


@dataclass(frozen=True)
class Index:
    """
    Base market index.

    Common concept for IBOR-style and overnight-style indices.
    """

    name: str
    currency: str


@dataclass(frozen=True)
class IborIndex(Index):
    """
    IBOR-style index, e.g. WIBOR 3M or EURIBOR 6M.
    """

    tenor_months: int
    fixing_lag_days: int


@dataclass(frozen=True)
class OvernightIndex(Index):
    """
    Overnight index, e.g. POLSTR, ESTR, SOFR.
    """

    fixing_lag_days: int
    observation_shift_days: int = 0
    compounding_method: str = "COMPOUNDED"
    rounding_digits: int | None = None

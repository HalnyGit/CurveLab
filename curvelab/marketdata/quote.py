from dataclasses import dataclass


@dataclass(frozen=True)
class MarketQuote:
    """
    Market quote used for curve construction.
    """

    market_key: str
    value: float

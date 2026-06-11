from dataclasses import dataclass

from curvelab.marketdata.quote import MarketQuote


@dataclass(frozen=True)
class MarketDataSet:
    """
    Market data snapshot for a given valuation date.
    """

    valuation_date: int
    quotes: list[MarketQuote]

    def get_quote(self, market_key: str) -> MarketQuote:
        for quote in self.quotes:
            if quote.market_key == market_key:
                return quote

        raise KeyError (f'Market quote not found: {market_key}')


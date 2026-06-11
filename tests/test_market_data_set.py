import pytest

from curvelab.marketdata.market_data_set import MarketDataSet
from curvelab.marketdata.quote import MarketQuote


def test_market_data_set_creation():
    quote = MarketQuote("PLN_DEPO_3M", 0.0525)

    data_set = MarketDataSet(
        valuation_date=1000,
        quotes=[quote],
    )

    assert data_set.valuation_date == 1000
    assert len(data_set.quotes) == 1
    assert data_set.quotes[0] == quote

def test_market_data_set_get_quote():
    quote = MarketQuote("PLN_DEPO_3M", 0.0525)

    data_set = MarketDataSet(
        valuation_date=1000,
        quotes=[quote],
    )

    result = data_set.get_quote("PLN_DEPO_3M")

    assert result == quote

def test_market_data_set_missing_quote_raises_error():
    data_set = MarketDataSet(
        valuation_date=1000,
        quotes=[],
    )

    with pytest.raises(KeyError):
        data_set.get_quote("PLN_DEPO_3M")
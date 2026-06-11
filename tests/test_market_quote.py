from curvelab.marketdata.quote import MarketQuote


def test_market_quote_creation():
    quote = MarketQuote(
        market_key="PLN_DEPO_3M",
        value=0.0525,
    )

    assert quote.market_key == "PLN_DEPO_3M"
    assert quote.value == 0.0525

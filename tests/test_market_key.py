import pytest

from curvelab.marketdata.market_key import MarketKey


def test_market_key_parses_deposit_key():
    key = MarketKey("PLN_DEPO_3M")

    assert key.currency == "PLN"
    assert key.instrument_type == "DEPO"
    assert key.tenor == "3M"


def test_market_key_parses_fra_key():
    key = MarketKey("PLN_FRA_1X4")

    assert key.currency == "PLN"
    assert key.instrument_type == "FRA"
    assert key.tenor == "1X4"


def test_market_key_parses_irs_key():
    key = MarketKey("PLN_IRS_2Y")

    assert key.currency == "PLN"
    assert key.instrument_type == "IRS"
    assert key.tenor == "2Y"


def test_market_key_raises_error_for_invalid_key():
    key = MarketKey("PLN_DEPO")

    with pytest.raises(ValueError):
        _ = key.parts

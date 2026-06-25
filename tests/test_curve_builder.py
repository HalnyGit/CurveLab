import pytest
from datetime import date

from curvelab.core.dates import date_to_internal_date
from curvelab.curves.curve_builder import CurveBuilder
from curvelab.curves.curve_definition import CurveDefinition
from curvelab.marketdata.market_data_set import MarketDataSet
from curvelab.marketdata.quote import MarketQuote


def test_curve_builder_builds_deposit_discount_curve():
    valuation_date = date_to_internal_date(date(2026, 1, 1))

    curve_definition = CurveDefinition(
        curve_name="PLN_WIBOR3M",
        market_keys=["PLN_DEPO_3M", "PLN_DEPO_6M"],
    )

    market_data_set = MarketDataSet(
        valuation_date=valuation_date,
        quotes=[
            MarketQuote("PLN_DEPO_3M", 0.05),
            MarketQuote("PLN_DEPO_6M", 0.06),
        ],
    )

    curve = CurveBuilder().build(
        curve_definition=curve_definition,
        market_data_set=market_data_set,
    )

    date_3m = date_to_internal_date(date(2026, 4, 1))
    date_6m = date_to_internal_date(date(2026, 7, 1))

    expected_df_3m = 1 / (1 + 0.05 * (90 / 365))
    expected_df_6m = 1 / (1 + 0.06 * (181 / 365))

    assert curve.get_df(date_3m) == pytest.approx(expected_df_3m)
    assert curve.get_df(date_6m) == pytest.approx(expected_df_6m)


def test_curve_builder_raises_for_unsupported_market_key():
    valuation_date = date_to_internal_date(date(2026, 1, 1))

    curve_definition = CurveDefinition(
        curve_name="PLN_WIBOR3M",
        market_keys=[
            "PLN_FRA_1X4",
        ],
    )

    market_data_set = MarketDataSet(
        valuation_date=valuation_date,
        quotes=[
            MarketQuote("PLN_FRA_1X4", 0.0525),
        ],
    )

    with pytest.raises(NotImplementedError):
        CurveBuilder().build(
            curve_definition=curve_definition,
            market_data_set=market_data_set,
        )

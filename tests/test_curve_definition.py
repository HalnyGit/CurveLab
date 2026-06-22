from datetime import date

from curvelab.core.dates import date_to_internal_date
from curvelab.curves.curve_definition import CurveDefinition


def test_curve_definition_creation():
    definition = CurveDefinition(
        curve_name="PLN_WIBOR3M",
        market_keys=[
            "PLN_DEPO_3M",
            "PLN_FRA_1X4",
            "PLN_FRA_2X5",
        ],
    )

    assert definition.curve_name == "PLN_WIBOR3M"
    assert definition.market_keys == [
        "PLN_DEPO_3M",
        "PLN_FRA_1X4",
        "PLN_FRA_2X5",
    ]

def test_curve_definition_returns_pillar_dates_for_depo_fra_irs():
    valuation_date = date_to_internal_date(date(2026, 1, 1))

    definition = CurveDefinition(
        curve_name="PLN_WIBOR3M",
        market_keys=[
            "PLN_DEPO_3M",
            "PLN_FRA_1X4",
            "PLN_FRA_2X5",
            "PLN_IRS_2Y",
        ],
    )

    expected_dates = [
        date_to_internal_date(date(2026, 4, 1)),
        date_to_internal_date(date(2026, 5, 1)),
        date_to_internal_date(date(2026, 6, 1)),
        date_to_internal_date(date(2028, 1, 1)),
    ]

    assert definition.pillar_dates(valuation_date) == expected_dates

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

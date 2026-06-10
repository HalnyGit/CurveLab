from curvelab.instruments.index import IborIndex, OvernightIndex


def test_ibor_index_creation():
    index = IborIndex(
        name="WIBOR_3M",
        currency="PLN",
        tenor_months=3,
        fixing_lag_days=2,
    )

    assert index.name == "WIBOR_3M"
    assert index.currency == "PLN"
    assert index.tenor_months == 3


def test_overnight_index_creation():
    index = OvernightIndex(
        name="POLSTR",
        currency="PLN",
        fixing_lag_days=1,
        observation_shift_days=0,
        compounding_method="COMPOUNDED",
        rounding_digits=8,
    )

    assert index.name == "POLSTR"
    assert index.currency == "PLN"
    assert index.compounding_method == "COMPOUNDED"

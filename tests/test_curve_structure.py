from curvelab.curves.curve_structure import CurveStructure


def test_curve_structure_creation():
    structure = CurveStructure(
        curve_name="PLN_WIBOR3M",
        pillar_dates=[365, 730],
    )

    assert structure.curve_name == "PLN_WIBOR3M"
    assert structure.pillar_dates == [365, 730]

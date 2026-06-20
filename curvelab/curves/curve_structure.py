from dataclasses import dataclass


@dataclass(frozen=True)
class CurveStructure:
    """
    Defines solver unknowns for a curve.
    """

    curve_name: str
    pillar_dates: list[int]

from dataclasses import dataclass

from curvelab.curves.curve import Curve


@dataclass(frozen=True)
class CurveSet:
    """
    Container for curves used in pricing and calibration.
    """

    curves: dict[str, Curve]

    def get(self, curve_name: str) -> Curve:
        return self.curves[curve_name]

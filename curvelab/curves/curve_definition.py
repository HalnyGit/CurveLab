from dataclasses import dataclass


@dataclass(frozen=True)
class CurveDefinition:
    """
    Defines how a curve is built.
    """

    curve_name: str
    market_keys: list[str]

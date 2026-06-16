## CurveBuilder
CurveBuilder currently assumes Act365.
Day count convention should come from market convention configuration.

## CurveSet - calibration problem
1. CurveSet
2. implied_quote(curve_set)
3. Deposit.implied_quote()
4. FRA.implied_quote()
5. CalibrationInstrument / residual
6. CalibrationProblem
7. Solver
8. CurveBuilder jako fasada

class FRA:
    def get_rate(self, curve_set):
        forecast_curve = curve_set.get(self.forecast_curve_name)
        return forward_rate(forecast_curve, self.start_date, self.end_date)
		
Najlepszy model w kodzie:

class CurveSet:
    def __init__(self, curves):
        self.curves = curves

    def get(self, curve_name):
        return self.curves[curve_name]

a produkt nie dostaje jednej krzywej:

prod.get_rate(curve)

tylko cały zestaw:

prod.get_rate(curve_set)

i sam wie z definicji instrumentu, których krzywych potrzebuje:

class FRA:
    def get_rate(self, curve_set):
        forecast_curve = curve_set.get(self.forecast_curve_name)
        return forward_rate(forecast_curve, self.start_date, self.end_date)

IRS:

class IRS:
    def get_rate(self, curve_set):
        forecast_curve = curve_set.get(self.float_forecast_curve_name)
        discount_curve = curve_set.get(self.discount_curve_name)

        float_pv = ...
        fixed_annuity = ...

        return float_pv / fixed_annuity

A Problem dostaje nie jedną listę DF-ów, tylko jeden wielki wektor niewiadomych:

x =
[
  discount_df_1,
  discount_df_2,
  discount_df_3,
  ...
  wibor3m_df_1,
  wibor3m_df_2,
  ...
  wibor6m_df_1,
  ...
]

W __call__() rozpakowujesz ten wektor do wielu krzywych:

def __call__(self, x):
    curve_set = self.curve_set_builder.build_from_vector(x)

    model_rates = np.array([
        product.get_rate(curve_set)
        for product in self.products
    ])

    return model_rates - self.market_rates

Czyli solver widzi nadal tylko:

F(x) = 0

ale Ty w środku masz cały świat:

x -> CurveSet -> Products -> model rates -> errors

W praktyce potrzebujesz więc obiektu typu:

CurveDefinition

który mówi:

PLN_LCH_DISCOUNT:
  pillars: ON, 1M, 3M, 6M, 9M, 1Y, 2Y, 3Y...
  instruments: WIBOR ON, WIBOR 1M, WIBOR 3M, FRA 3x6, FRA 6x9, IRS 2Y...

PLN_WIBOR_3M:
  pillars: 3M, 6M, 9M, 1Y...
  instruments: FRA 3x6, FRA 6x9, IRS 2Y...

PLN_WIBOR_6M:
  ...

I jeszcze mapowania:

IRS PLN 6M:
  forecast_curve = PLN_WIBOR_6M
  discount_curve = PLN_LCH_DISCOUNT



class CurveSetCalibrationProblem:
    ...
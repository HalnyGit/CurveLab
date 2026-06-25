NOW:
                 MarketDataSet
                       │
                       ▼
               CurveDefinition
                 (market_keys)
                       │
                       ▼
          CurveBuilder (bootstrap v1)
                       │
                       ▼
                    Curve
                       │
                       ▼
                   CurveSet
                       │
                       ▼
                PricingContext
                       │
                       ▼
                    Products
             Deposit / FRA / IRS
                       │
                       ▼
                  model_rate()
				  
				  

AIM:
                 MarketDataSet
                       │
                       ▼
               CurveDefinition
                       │
                       ▼
        CurveSetCalibrationProblem
                       ▲
                       │
                 CurveSetBuilder
                       ▲
                       │
              Solver (scipy.optimize)				  
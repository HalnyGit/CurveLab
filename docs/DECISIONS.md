2026-05-29

Decision:
Internal dates stored as integers.

Reason:
Excel/.NET integration.

---

Decision:
Products generate cashflows only.

Reason:
Separation of pricing logic.

---

2026-05-30

Decision:
CurveLab stores dates internally as integers representing the number of calendar days since 2000-01-01.

Examples:
2000-01-01 = 0
2000-01-02 = 1

Rationale:
Simple date arithmetic
Easy integration with Excel
Easy integration with future .NET components
Simple serialization between systems
Avoids locale and regional date format issues
Independent from Excel serial date implementation

Consequences:
All external dates must be converted at system boundaries.
Excel adapters convert between internal dates and Excel dates.
.NET adapters convert between internal dates and DateTime.
Human-readable dates are not used as the internal calculation format inside the pricing engine.
Internal calculations use integer dates.
Human-readable dates may be exposed for:
- logging
- debugging
- test assertions
- reports
- Excel / UI / API output

---

Decision:
Create curvelab/core/dates.py

Reason:
Date handling is a first-class concern in a pricing engine

Consequences:
- All date conversions are centralized.
- Internal date representation is implemented in a single location.
- Future schedule and calendar functionality can build upon this module.
- Curve, Cashflow and Pricing components do not implement their own date conversion logic.
- curvelab/core/dates.py

---

Decision:
Day count convention is treated as an explicit pricing parameter.

Reason:
Traders must be able to select or verify the appropriate day count convention when pricing trades.

Consequences:
- Day count is not hardcoded inside products.
- Day count conventions are passed explicitly to instruments, legs or curve builders.
- Future GUI / Excel interfaces must expose day count convention as a configurable or visible parameter.
- Pricing results should be explainable in terms of the day count convention used.
- curvelab/core/daycount.py

---

Decision:
CurveLab uses a hybrid architecture.

Domain concepts are represented by lightweight objects.
Numerical calculations are implemented as explicit functions.

Reason:
The system should remain easy to understand and extend, while still supporting efficient batch pricing.
Balance between maintainability, transparency and performance.

Domain concepts are represented by lightweight objects.

Examples:
- Trade
- Curve
- CurveSet
- Schedule
- DayCount

Numerical calculations are implemented as dedicated functions and pricing engines.

Examples:
- Interpolation
- Discount factor calculations
- Present value calculations
- Risk calculations

Consequences:
- Products generate cashflows.
- Products do not calculate PV directly.
- Pricing logic is separated from trade representation.
- Heavy calculations should avoid unnecessary object creation.
- Future batch pricing should support efficient array-based calculations.

---

Decision:
Day count convention is treated as a first-class component.

Reason:
Day count conventions materially impact accrual calculations, forward rates and present values.
They are part of trade and market conventions, not merely an implementation detail.

Consequences:
- Day count conventions are represented explicitly.
- Products, schedules and curves may depend on a day count convention.
- Future GUI and Excel integrations should expose the convention used.
- Pricing results should be explainable in terms of the selected convention.
- A DayCount base class will be defined.
- Specific conventions derive from DayCount.
- Products, schedules and curves interact through the common interface.
- GUI and Excel integrations expose convention names, not implementation classes.

---

Decision:
Create a modular package structure under curvelab/.

Reason:
Separate core utilities, curves, instruments, pricing and market data from the beginning.

Consequences:
- Date and day count logic lives in curvelab/core.
- Curve logic lives in curvelab/curves.
- Product definitions live in curvelab/instruments.
- Pricing engines live in curvelab/pricing.
- Market data handling lives in curvelab/marketdata.

---

2026-05-31

Decision:
CurveLab should avoid becoming a mini-QuantLib.

Reason:
The project should remain practical, readable, lightweight, trader-friendly and extensible.

Consequences:
- Avoid unnecessary abstractions.
- Add abstractions only when they solve a real problem.
- Prefer simple APIs.
- Prioritize explainability over architectural complexity.
- Keep future extensions possible without overengineering the MVP.
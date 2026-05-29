# CurveLab Architecture

## Core Principles

### Internal Dates

Dates are stored internally as integers.

Rationale:
- Easy Excel integration
- Easier integration with potential future .NET components
- Simple serialization between systems
- Faster calculations
- Reduced risk of locale / regional date format issues

### Product Architecture

Instrument
-> Cashflows
-> Pricer
-> PV

Products do not calculate PV directly.
Pricing is performed by dedicated pricing engines.

Important:
- Human-readable dates are used only at system boundaries.
- Input adapters convert external dates into internal integer dates.
- Output adapters convert internal integer dates back into Excel / UI / API formats.

### Curves

Forecast Curve != Discount Curve

### Market Data

Market data is separated from pricing logic.

### Future Direction

On-demand curve building with cache.

### Currency and Collateral

Cashflows, curves and market data are currency-aware.

Collateral currency is treated as an explicit pricing parameter.

Examples:

- PLN cashflows collateralized in PLN
- PLN cashflows collateralized in EUR
- EUR cashflows collateralized in USD

The pricing engine must always know:
- Flow Currency
- Forecast Curve
- Discount Curve
- Collateral Currency

### Separation of Concerns

Responsibilities are separated into dedicated components.

Instrument:
- Generates cashflows

Curve:
- Provides discount factors and forward rates

Pricer:
- Calculates PV and risk measures

Market Data:
- Provides market quotes

Curve Builder:
- Builds curves from market data

No component should perform responsibilities belonging to another component.


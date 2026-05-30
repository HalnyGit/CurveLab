# CurveLab Architecture

## Core Principles

### Internal Dates

Dates are stored internally as integers.
Internal Date Standard:

- Epoch: 2000-01-01
- Internal date = number of calendar days since epoch

Examples:

- 2000-01-01 = 0
- 2000-01-02 = 1

Human-readable dates are converted at system boundaries.

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

## Development Philosophy

CurveLab development follows two parallel tracks.

### Track 1 – CurveLab

Focus:

* Architecture
* Python implementation
* Curves
* Products
* Pricing engines
* Market data
* Testing

Goal:
Build a production-quality multicurve pricing framework.

### Track 2 – Quant Fundamentals

Focus:

* Time value of money
* Discount factors
* Forward rates
* Day count conventions
* Interpolation
* Bootstrapping
* Numerical methods
* Stochastic processes
* Derivatives pricing theory

Goal:
Understand the mathematical and financial concepts behind the implementation.

### Guiding Principle

Every major CurveLab component should be understood on three levels:

1. Market intuition
2. Mathematical formulation
3. Python implementation

The preferred learning path is:

Market intuition
→ Mathematical formulation
→ Python implementation

rather than the reverse.

### Design Priorities

Priority order:

1. Correctness
2. Transparency
3. Maintainability
4. Performance

### Design Goals

CurveLab should be:

- Practical
- Readable
- Lightweight
- Easy to use by traders
- Extensible

The goal is not to recreate QuantLib.

The system should support the current MVP scope:

- FRA
- IRS
- OIS
- Curves
- Discounting
- Multi-curve pricing

but remain open for future extensions such as:

- CCS
- MTM CCS
- FX products
- Cap/Floor
- Swaptions
- More advanced risk measures

# Curves

## Purpose

This document describes curve types supported by CurveLab and their construction methodology.

## Curve Types

### Discount Curve

Purpose:

* Discount future cashflows.

Examples:

* PLN OIS
* EUR OIS
* PLN collateralized in EUR
* EUR collateralized in USD

---

### Forecast Curve

Purpose:

* Forecast future floating rates.

Examples:

* WIBOR 3M
* WIBOR 6M
* EURIBOR 3M
* EURIBOR 6M
* POLSTR
* ESTR

---

### Interpolation

Interpolation strategy is part of curve configuration.

Different interpolation methods may be used
for different curve types and curve segments.

---

## OIS Reference Rates

Examples:

- POLSTR
- €STR
- SOFR
- SONIA

Purpose:

These rates serve as the foundation for modern collateralized valuation frameworks.

Usage:

- OIS valuation
- OIS curve construction
- Discount curve construction
- Collateral discounting
- Cross-currency discounting

Notes:

Unlike traditional IBOR indices (e.g. WIBOR or EURIBOR),
OIS reference rates are used both for forecasting overnight cashflows
and as the foundation of discount curves used in collateralized pricing.

Examples:

- WIBOR → PLN Discount Curve
- POLSTR → PLN OIS Discount Curve
- €STR → EUR OIS Discount Curve
- SOFR → USD OIS Discount Curve
- SONIA → GBP OIS Discount Curve

---

## Future Topics

* Interpolation
* Bootstrap Methodology
* FX Forward Curves
* Collateral Discounting
* Cross Currency Curves
* Curve Dependencies
* Curve Cache
* On-Demand Curve Building

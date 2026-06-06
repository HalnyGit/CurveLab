# Pricer Roadmap

## Założenia

Tempo pracy:

* 1–2h dziennie
* 5 dni w tygodniu
* Sprinty 2-tygodniowe

## Cel projektu

Stworzenie własnego silnika wyceny instrumentów stopy procentowej z obsługą:

* FRA
* IRS
* OIS

oraz

* Forecast Curves
* Discount Curves
* Collateral Discounting
* Multicurrency Discounting

Docelowo:

* CCS
* MTM CCS
* FX Forwards
* FX Swaps
* Real-Time Market Data
* Excel Integration

---

# Faza 0 – Organizacja Projektu

## Sprint 0

### Cel

Przygotowanie repozytorium i dokumentacji.

### Zadania

* [X] Utworzyć repozytorium
* [X] Utworzyć katalog docs
* [X] Utworzyć ARCHITECTURE.md
* [X] Utworzyć ROADMAP.md
* [X] Utworzyć CURVES.md
* [X] Utworzyć PRODUCTS.md
* [X] Przygotować .gitignore

### Rezultat

Gotowy szkielet projektu.

---

# Faza 1 – Fundament

## Sprint 1

### Cel

Podstawowe klasy infrastrukturalne.

### Zadania

* [X] DayCount
* [ ] LinearInterpolator
* [ ] DiscountCurve
* [ ] Testy interpolacji
* [ ] Testy krzywych

### Rezultat

Działająca krzywa discountowa.

---

## Sprint 2

### Cel

Framework cashflowów.

### Zadania

* [X] Period
* [X] Schedule
* [ ] Cashflow
* [ ] Pricer
* [ ] Testy PV

### Rezultat

Możliwość wyceny dowolnej listy cashflowów.

---

# Faza 2 – FRA i Bootstrap

## Sprint 3

### Cel

Implementacja FRA.

### Zadania

* [ ] FRA Product
* [ ] Forward Rate Calculation
* [ ] FRA Repricing Tests

### Rezultat

FRA reprices market quote.

---

## Sprint 4

### Cel

Bootstrap pierwszej krzywej.

### Zadania

* [ ] Refaktoryzacja klasy Problem
* [ ] CurveBuilder
* [ ] Bootstrap FRA Curve
* [ ] Repricing Tests

### Rezultat

Pierwsza działająca forecast curve.

---

# Faza 3 – FX i Collateral Discounting

## Sprint 5

### Cel

Obsługa FX Spot i FX Forward.

### Zadania

* [ ] FX Spot
* [ ] FX Forward Curve
* [ ] FX Forward Interpolation
* [ ] Testy FX

### Rezultat

Działająca krzywa FX Forward.

---

## Sprint 6

### Cel

Discounting w walucie innej niż flow.

### Zadania

* [ ] EUR Discount Curve
* [ ] PLN Discount Curve under EUR Collateral
* [ ] FX-based Discount Factors
* [ ] Repricing Tests

### Rezultat

Możliwość wyceny:

* PLN flow collateralized in EUR
* EUR flow collateralized in PLN

---

# Faza 4 – IRS

## Sprint 7

### Cel

Implementacja IRS.

### Zadania

* [ ] FixedLeg
* [ ] FloatingLeg
* [ ] Cashflow Generation

### Rezultat

Działające nogi IRS.

---

## Sprint 8

### Cel

Par Rate IRS.

### Zadania

* [ ] IRS Product
* [ ] IRS Par Rate
* [ ] IRS Repricing Tests

### Rezultat

Pełna wycena IRS.

---

# Faza 5 – OIS

## Sprint 9

### Cel

Implementacja OIS.

### Zadania

* [ ] OIS Product
* [ ] OIS Cashflows
* [ ] OIS Tests

### Rezultat

Działający produkt OIS.

---

## Sprint 10

### Cel

Bootstrap krzywych OIS.

### Zadania

* [ ] PLN OIS Curve
* [ ] EUR OIS Curve
* [ ] Repricing Tests

### Rezultat

Działające krzywe OIS.

---

# Faza 6 – Multi Curve Framework

## Sprint 11

### Cel

Rozdzielenie Forecast i Discount Curve.

### Zadania

* [ ] ForecastCurve
* [ ] DiscountCurve
* [ ] Curve Interfaces
* [ ] Refaktoryzacja produktów

### Rezultat

Nowoczesny framework multi-curve.

---

## Sprint 12

### Cel

Trader Ready MVP.

### Zadania

* [ ] PV
* [ ] DV01
* [ ] Curve Bumping
* [ ] Sensitivity Tests

### Rezultat

Obsługa:

* FRA
* IRS
* OIS

dla:

* PLN
* EUR

z możliwością:

* discountingu w innej walucie niż flow
* PV
* DV01

---

# Wersja 2.0

## Produkty

* CCS
* MTM CCS
* FX Swap

## Krzywe

* PLN collateralized in EUR
* PLN collateralized in USD
* EUR collateralized in USD
* EUR collateralized in PLN

budowane z:

* FX Spot
* FX Forwards
* CCS Quotes

## Architektura

* Curve Cache
* Curve Manager
* Dependency Graph
* On-The-Fly Curve Building

## Integracje

* Excel Add-In
* GUI
* SQL Database
* Real-Time Market Data

---

# Definicja sukcesu MVP

Możliwość wyceny:

* FRA
* IRS
* OIS

w PLN i EUR

przy użyciu:

* Forecast Curves
* Discount Curves
* FX Forwards
* Collateral Discounting

oraz wyliczenia:

* PV
* Par Rate
* DV01

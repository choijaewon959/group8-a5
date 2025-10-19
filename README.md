# Assignment 5: Testing & CI in Financial Engineering

[![CI](https://github.com/choijaewon959/group8-a5/actions/workflows/ci.yml/badge.svg)](https://github.com/choijaewon959/group8-a5/actions/workflows/ci.yml)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.11-blue)

A lightweight, deterministic daily backtesting system for quantitative trading strategies with comprehensive testing and CI/CD pipeline.

## 🏗️ Design Architecture

### Core Components

* **PriceLoader** (`price_loader.py`): Loads market data from CSV files, returns pandas Series of prices
* **Strategy** (`strategy.py`): Implements volatility breakout strategy with configurable parameters (k, window)
* **Broker** (`broker.py`): Simulates order execution with cash/position tracking (no slippage/fees)
* **Backtester** (`engine.py`): Orchestrates end-of-day trading loop: signal generation → order execution → performance tracking

### Design Principles

- **Deterministic**: No randomness for reproducible testing
- **Modular**: Clear separation of concerns between components
- **Testable**: Each component can be unit tested in isolation
- **Error Handling**: Comprehensive validation and meaningful error messages
- **Type Hints**: Full type annotation for better code maintainability

## � Repository Structure

```
group8-a5/
├── backtester/                 # Core trading system
│   ├── broker.py              # Order execution and portfolio management
│   ├── engine.py              # Main backtesting engine
│   ├── price_loader.py        # Market data loading
│   └── strategy.py            # Volatility breakout strategy
├── tests/                     # Comprehensive test suite
│   ├── conftest.py           # Shared test fixtures
│   ├── test_broker.py        # Broker component tests
│   ├── test_engine.py        # Backtester engine tests
│   └── test_strategy.py      # Strategy component tests
├── data/
│   └── market_data.csv       # Sample market data
├── .github/workflows/
│   └── ci.yml               # GitHub Actions CI pipeline
├── htmlcov/                 # Coverage HTML reports
├── pyproject.toml           # Project configuration
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

## 🚀 How to Run Tests

### Prerequisites
```bash
pip install -r requirements.txt
```

### Running Tests
```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest tests/test_strategy.py

# Run with coverage
coverage run -m pytest -q
coverage report -m
```

### Generate Coverage Report
```bash
# Terminal report
coverage report -m

# HTML report (opens in browser)
coverage html
open htmlcov/index.html
```

### Validate Coverage Threshold
```bash
coverage report --fail-under=90
```

## 🔄 CI/CD Pipeline Status

![CI Status](https://github.com/choijaewon959/group8-a5/actions/workflows/ci.yml/badge.svg)

### Pipeline Configuration
- **Trigger**: Push and Pull Request events
- **Platform**: Ubuntu Latest
- **Python Version**: 3.11
- **Steps**:
  1. Checkout code
  2. Setup Python environment
  3. Install dependencies
  4. Run tests with coverage
  5. Validate 90% coverage threshold

### Workflow File: `.github/workflows/ci.yml`
```yaml
name: Assignment 5 - testing and CI Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: coverage run -m pytest -q
      - run: coverage report --fail-under=90
```

## 📊 Coverage Summary

### Current Coverage: **100%** ✅

```
Name                     Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------------------
backtester/broker.py        21      0     12      0   100%
backtester/engine.py        14      0      2      0   100%
backtester/strategy.py      17      0      4      0   100%
--------------------------------------------------------------------
TOTAL                       52      0     18      0   100%
```

### Coverage Configuration
- **Source**: `backtester/` package
- **Omitted**: `tests/` and `backtester/price_loader.py` (simple data loading)
- **Branch Coverage**: Enabled
- **Minimum Threshold**: 90%
- **Report**: Shows missing lines and branch coverage

## 🧪 Testing Strategy

### Test Fixtures (`conftest.py`)
- **prices**: Deterministic rising price series (100→120, 200 points)
- **strategy**: Default VolatilityBreakoutStrategy instance
- **broker**: Broker with $1,000 initial cash

### Test Coverage
1. **Strategy Tests**: Signal generation, edge cases, error handling
2. **Broker Tests**: Order execution, cash management, position tracking
3. **Engine Tests**: End-to-end backtesting workflow, equity calculations

### Key Test Scenarios
- Normal market conditions
- Edge cases (insufficient funds, invalid orders)
- Error conditions (negative prices, short data series)
- Boundary conditions (zero quantities, exact matches)

## 📈 Example Usage

```python
from backtester.engine import Backtester
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker
from backtester.price_loader import load_data
import pandas as pd

# Load data and setup components
data = load_data()
strategy = VolatilityBreakoutStrategy(k=0.5, window=10)
broker = Broker(cash=1_000_000)

# Run backtest
backtester = Backtester(strategy, broker)
final_equity = backtester.run(pd.Series(data.values.ravel()))
```

## ✅ Deliverables Status

- ✅ **Code Components**: All four core components implemented with clean, readable code
- ✅ **Unit Tests**: Comprehensive test suite with 17 passing tests using shared fixtures
- ✅ **CI Pipeline**: GitHub Actions workflow passing successfully
- ✅ **Coverage**: 100% coverage exceeding 90% requirement
- ✅ **Documentation**: Complete README with design notes, testing guide, and CI status

---

*Assignment completed for FINM 325 - Financial Engineering at University of Chicago*


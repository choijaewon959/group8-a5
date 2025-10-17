# Assigment 5: Testing & CI in Financial Engineering

A tiny daily backtester with:

* **PriceLoader:** returns a `pandas.Series` of prices for a single symbol (use synthetic data for tests).
* **Strategy:** outputs daily signals (`-1, 0, +1` or booleans) from price history.
* **Broker:** accepts market orders, updates cash/position with no slippage/fees (keep deterministic for tests).
* **Backtester:** runs end-of-day loop: compute signal (t−1), trade at close (t), track cash/position/equity.

> You’ll implement **one simple strategy** (e.g., *VolatilityBreakoutStrategy*).
> This strategy calculates a rolling x-day standard deviation of returns and buys when 
> the current return is > this x-day figure.
> 
> The assignment is graded on **tests + CI**, not alpha.

---

## ⚙️ Constraints

* Tests must **not** hit the network or external APIs — *mock or generate data.*
* Test suite must complete in **< 60 seconds** on GitHub Actions.
* Coverage **fails CI** if `< 90%` (branches optional, lines required).

---

## 🗂️ Repository Layout (Suggested)

```
trading-ci-lab/
  backtester/
    __init__.py
    price_loader.py
    strategy.py
    broker.py
    engine.py
  tests/
    test_strategy.py
    test_broker.py
    test_engine.py
    conftest.py
  requirements.txt
  pyproject.toml        # or setup.cfg for pytest/coverage options
  .github/workflows/ci.yml
  README.md
```

---

### requirements.txt

```
pytest
coverage
pandas
numpy
```

> 💡 *Tip:* Add a coverage badge locally with `coverage-badge` (optional).

---

# My Project
![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen)


## 🧩 Part 2 — Minimal Components (45–60 min)

Implement only what you need to support tests:

```python
# backtester/strategy.py
import numpy as np
import pandas as pd

class VolatilityBreakoutStrategy:
    
    def __init__(self):
        pass

    def signals(self, prices: pd.Series) -> pd.Series:
        pass
```

```python
# backtester/broker.py
class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):
        pass
```

```python
# backtester/engine.py
import pandas as pd

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):
        pass
```

---

### Example Fixtures & Mocks

```python
# tests/conftest.py
import numpy as np, pandas as pd, pytest
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker

@pytest.fixture
def prices():
    # deterministic rising series
    return pd.Series(np.linspace(100, 120, 200))

@pytest.fixture
def strategy():
    return VolatilityBreakoutStrategy()

@pytest.fixture
def broker():
    return Broker(cash=1_000)
```

```python
# tests/test_strategy.py
def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)
```

```python
# tests/test_broker.py
import pytest

def test_buy_and_sell_updates_cash_and_pos(broker):
    broker.market_order("BUY", 2, 10.0)
    assert (broker.position, broker.cash) == (2, 1000 - 20.0)

def test_rejects_bad_orders(broker):
    with pytest.raises(ValueError):
        broker.market_order("BUY", 0, 10)
```

```python
# tests/test_engine.py
from unittest.mock import MagicMock
from backtester.engine import Backtester

def test_engine_uses_tminus1_signal(prices, broker, strategy, monkeypatch):
    # Force exactly one buy at t=10 by controlling signals
    fake_strategy = MagicMock()
    fake_strategy.signals.return_value = prices*0
    fake_strategy.signals.return_value.iloc[9] = 1  # triggers buy at t=10
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    assert broker.position == 1
    assert broker.cash == 1000 - float(prices.iloc[10])
```

---

## 🧩 Part 4 — Coverage & Reporting (30–45 min)

Run locally:

```bash
coverage run -m pytest -q
coverage report -m
coverage html
```

```bash
coverage report --fail-under=90
```

Commit the HTML report (optional) or attach screenshots in the README.

---

## ✅ Deliverables (Checklist)

* [ ] Code for `PriceLoader`, `Strategy`, `Broker`, `Backtester` (minimal but clean).
* [ ] `tests/` with comprehensive unit tests and fixtures.
* [ ] Passing GitHub Actions run (link/screenshot).
* [ ] Coverage report showing **≥ 90%**.
* [ ] `README.md` with design notes, how to run tests, CI status, coverage summary.

---


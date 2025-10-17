# Assigment 5: Testing & CI in Financial Engineering
![Coverage](https://img.shields.io/badge/coverage-92%25-brightgreen)


A tiny daily backtester with:

* **PriceLoader:** returns a `pandas.Series` of prices for a single symbol (use synthetic data for tests).
* **Strategy:** outputs daily signals (`-1, 0, +1` or booleans) from price history.
* **Broker:** accepts market orders, updates cash/position with no slippage/fees (keep deterministic for tests).
* **Backtester:** runs end-of-day loop: compute signal (t−1), trade at close (t), track cash/position/equity.

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


# tests/test_strategy.py
import pandas as pd
import numpy as np
import pytest

# given 
def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)

# check output is digit{-1,0,1}
def test_signals_are_in_valid_range(strategy, prices):
    sig = strategy.signals(prices)
    assert set(sig.dropna().unique()).issubset({-1, 0, 1})

# check NaN value exist 
def test_nan_handling(strategy, prices):
    prices.iloc[3] = np.nan
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)

# check price movement 
def test_constant_prices(strategy, prices):
    if prices.nunique() == 1:
        sig = strategy.signals(prices)
        assert all(sig == 0)

# check negative prices then occur 
def test_negative_prices(strategy):
    neg_prices = pd.Series([100, -105, 102, -108, 107])
    with pytest.raises(ValueError, match="Prices must be non-negative"):
        strategy.signals(neg_prices)


# check infinite prices then excpet
def test_infinite_prices(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)
    assert set(sig.dropna().unique()).issubset({-1, 0, 1})


# check all Nan then send all 0('Hold') as signals 
def test_all_nan_series(strategy, prices):
    prices[:] = [np.nan]*len(prices)
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)
    assert set(sig.dropna().unique()) == {0}

# Strategy logic: signal generation of x-day volatility breakout
def test_shorter_than_window_raises_error(strategy, prices):
    short_prices = prices[:5] 
    with pytest.raises(ValueError, match=f"Price series must have at least 10 points"):
        strategy.signals(short_prices)

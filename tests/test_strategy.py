import pandas as pd
import numpy as np
# given 
def test_signals_length(strategy, prices):
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)


# check output is digit{-1,0,1}
def test_signals_are_in_valid_range(strategy, prices):
    sig = strategy.signals(prices)
    assert set(sig.dropna().unique()).issubset({-1, 0, 1})


# check NaN value exist 
def test_nan_handling(strategy):
    prices = pd.Series(np.linspace(100, 110, 10))
    prices.iloc[3] = np.nan
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)


import pandas as pd
import numpy as np

class VolatilityBreakoutStrategy:
    def __init__(self, k=0.5, window=10):
        self.k = k
        self.window = window

    def signals(self, prices: pd.Series):
        # exception for negative price
        if (prices < 0).any():
            raise ValueError("Prices must be non-negative") 
        # exception for short data amount 
        if len(prices) < self.window:
            raise ValueError(f"Price series must have at least {self.window} points")

        signals = pd.Series(0, index=prices.index)
        
        returns = prices.pct_change().fillna(0)
        rolling_std = returns.rolling(self.window).std().fillna(0)
        threshold = rolling_std * self.k
        signals[returns > threshold] = 1
        signals[returns < -threshold] = -1
        
        return signals

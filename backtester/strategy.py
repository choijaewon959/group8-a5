import pandas as pd
import numpy as np

class VolatilityBreakoutStrategy:
    def __init__(self, k=0.5):
        self.k = k

    def signals(self, prices: pd.Series):
        # exception handling 'Negative' price
        if (prices < 0).any():
            raise ValueError("Prices must be non-negative") 

        signals = pd.Series(0, index=prices.index)
        if len(prices) > 1:
            returns = prices.pct_change().fillna(0)
            threshold = returns.std() * self.k
            signals[returns > threshold] = 1   
            signals[returns < -threshold] = -1 
        return signals

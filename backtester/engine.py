import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backtester.strategy import VolatilityBreakoutStrategy
from backtester.broker import Broker
import pandas as pd
from backtester.price_loader import load_data

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):
        signals = self.strategy.signals(prices)

        signals = signals.replace({1:"BUY", 0:"HOLD", -1:"SELL"})

        for idx, sig in enumerate(signals[:-1]):
            self.broker.market_order(sig, 1, prices[idx+1])

        equity = self.broker.cash + self.broker.position * prices.iloc[-1]
        return equity
"""
data = load_data()
backT = Backtester(VolatilityBreakoutStrategy(), Broker())
backT.run(pd.Series(data.values.ravel()))
"""



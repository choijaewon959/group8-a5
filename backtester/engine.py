from strategy import VolatilityBreakoutStrategy
from broker import Broker
import pandas as pd

class Backtester:
    def __init__(self, strategy, broker):
        self.strategy = strategy
        self.broker = broker

    def run(self, prices: pd.Series):
        signals = self.strategy.run(prices)

        for idx, sig in enumerate(signals):
            self.broker.market_order(sig[0], 1, prices[idx])

backT = Backtester(VolatilityBreakoutStrategy(), Broker())
#prices = pd.read_csv('market_prices.csv')
backT.run(prices)



import numpy as np, pandas as pd, pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
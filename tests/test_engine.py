# tests/test_engine.py
from unittest.mock import MagicMock
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backtester.engine import Backtester
from backtester.strategy import VolatilityBreakoutStrategy
import pandas as pd

# Force exactly one buy at t=10 by controlling signals
def test_engine_uses_tminus1_signal(prices, broker, strategy, monkeypatch):
    fake_strategy = MagicMock()
    fake_strategy.signals.return_value = prices*0
    fake_strategy.signals.return_value.iloc[9] = 1  # triggers buy at t=10
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    assert broker.position == 1
    assert broker.cash == 1000 - float(prices.iloc[10])


#test final equity matches cash + pos*price
def test_equity_matches_cash_and_posprice(prices, broker, strategy, monkeypatch):
    fake_strategy = MagicMock()
    fake_strategy.signals.return_value = prices*0
    fake_strategy.signals.return_value.iloc[9] = 1
    fake_strategy.signals.return_value.iloc[19] = -1
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)
    expected_equity = broker.cash + broker.position * prices.iloc[-1]
    assert eq == expected_equity

#test if engine executes trades
def test_engine_executes_trades(prices, broker, strategy, monkeypatch):
    fake_strategy = MagicMock()
    fake_strategy.signals.return_value = prices*0
    fake_strategy.signals.return_value.iloc[0] = 1
    fake_strategy.signals.return_value.iloc[2] = -1

    broker.market_order = MagicMock()
    bt = Backtester(fake_strategy, broker)
    eq = bt.run(prices)

    #test if engine runs market_order for each price
    assert broker.market_order.call_count==len(prices)-1

    #test if calls are correct for price t: signal, quantity & price[t+1]
    calls = broker.market_order.call_args_list
    first_call = calls[0][0]
    assert first_call[0] == "BUY"
    assert first_call[1] == 1
    assert first_call[2] == prices.iloc[1]

    third_call = calls[2][0]
    assert third_call[0] == "SELL"
    assert third_call[1] == 1
    assert third_call[2] == prices.iloc[3]







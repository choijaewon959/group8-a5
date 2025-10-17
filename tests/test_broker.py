# tests/test_broker.py
import pytest

def test_buy_and_sell_updates_cash_and_pos(broker):
    broker.market_order("BUY", 2, 10.0)
    assert (broker.position, broker.cash) == (2, 1000 - 20.0)

def test_rejects_bad_orders(broker):
    with pytest.raises(ValueError):
        broker.market_order("BUY", 0, 10)

def test_rejects_insufficient_cash(broker):
    with pytest.raises(ValueError):
        broker.market_order("BUY", 200, 10)

def test_rejects_insufficient_position(broker):
    with pytest.raises(ValueError):
        broker.market_order("SELL", 1, 10)
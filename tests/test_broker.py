# tests/test_broker.py
import pytest

BUY = "BUY"
SELL = "SELL"
HOLD = "HOLD"
SIDE_BAD = "SIDE_BAD"

def test_buy_and_sell_updates_cash_and_pos(broker):
    buy_qty = 2
    buy_price = 10.0
    sell_qty = 1
    sell_price = 15.0

    broker.market_order(BUY, buy_qty, buy_price)
    assert broker.position == buy_qty
    assert broker.cash == 1000 - (buy_qty * buy_price)

    broker.market_order(SELL, sell_qty, sell_price)
    assert broker.position == buy_qty - sell_qty
    assert broker.cash == 1000 - (buy_qty * buy_price) + (sell_qty * sell_price)

def test_rejects_bad_orders(broker):
    with pytest.raises(ValueError):
        broker.market_order(BUY, 0, 10)

def test_rejects_insufficient_cash(broker):
    with pytest.raises(ValueError):
        broker.market_order(BUY, 200, 10)

def test_rejects_insufficient_position(broker):
    with pytest.raises(ValueError):
        broker.market_order(SELL, 1, 10)

def test_bad_side(broker):
    with pytest.raises(ValueError):
        broker.market_order(SIDE_BAD, 1, 10)

def test_hold(broker):
    cash = broker.cash
    pos = broker.position
    broker.market_order(HOLD, 999, 999)  # qty & price should not matter
    assert broker.cash == cash
    assert broker.position == pos

def test_bad_side(broker):
    with pytest.raises(ValueError):
        broker.market_order(SIDE_BAD, 1, 10)
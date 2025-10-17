class Broker:
    def __init__(self, cash: float = 1_000_000):
        self.cash = cash
        self.position = 0

    def market_order(self, side: str, qty: int, price: float):
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        if side == "BUY":
            cost = qty * price
            if cost > self.cash:
                raise ValueError("Insufficient cash for buy order")
            self.cash -= cost
            self.position += qty
        elif side == "SELL":
            if qty > self.position:
                raise ValueError("Insufficient position for sell order")
            self.cash += qty * price
            self.position -= qty
        else:
            raise ValueError("Side must be 'BUY' or 'SELL'")
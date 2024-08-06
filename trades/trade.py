from abc import ABC, abstractmethod
from decimal import Decimal

class Trade(ABC):
    exchange = {"NYSE", "NASDAQ", "CHX"}
    sides = {"buy", "sell"}

    def __init__(self, trade_id: str, exchange: str, symbol: str, price: Decimal, quantity: int, side: str):
        if not trade_id:
            raise ValueError("Trade ID cannot be empty.")
        if exchange not in self.exchange:
            raise ValueError(f"Incorrect exchange! It should be {exchange}")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if side not in self.sides:
            raise ValueError(f"Incorrect side: {side}. Must be 'buy' or 'sell'.")

        self.trade_id = trade_id  # a unique trade ID
        self.exchange = exchange  # the place the trade took place
        self.symbol = symbol  # the company name
        self.price = price  # the price of the trade as USD
        self.quantity = quantity  # the quantity traded
        self.side = side  # the side(buy or sell)


    @abstractmethod
    def value(self) -> Decimal:
        pass

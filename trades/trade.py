from abc import ABC, abstractmethod
from decimal import Decimal


class Trade(ABC):
    def __init__(self, trade_id: str, exchange: str, symbol: str, price: Decimal, quantity: int, side: str):
        self.trade_id = trade_id  # a unique trade ID
        self.exchange = exchange  # a code that identifies the exchange where the trade took place
        self.symbol = symbol  # a symbol that identifies what was traded
        self.price = Decimal(price)  # a price that the trade was executed at (priced in US Dollars and Cents)
        self.quantity = quantity  # the quantity traded
        self.side = side  # the side (buy or sell)

        @abstractmethod
        def value(self) -> Decimal:
            pass


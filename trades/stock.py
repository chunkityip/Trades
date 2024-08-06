from .trade import Trade
from decimal import Decimal


class Stock(Trade):

    def __str__(self):
        return (f"Trade ID: {self.trade_id}, "
                f"Exchange: {self.exchange}, " 
                f"Symbol: {self.symbol}, "
                f"Price: {self.price}, "
                f"Quantity: {self.quantity}, "
                f"Side: {self.side}")

    __repr__ = __str__

    # def __repr__(self):
    #     return self.__str__()

    def value(self) -> Decimal:
        return self.price * self.quantity

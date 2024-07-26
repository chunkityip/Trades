from decimal import Decimal
from trade import Trade

# This class can be Bond trades , Futures trades and Forex trades

class StockTrade(Trade):
    def value(self) -> Decimal:
        return self.price * self.quantity
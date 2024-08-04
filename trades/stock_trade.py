from decimal import Decimal
from .trade import Trade


# This class can be Bond trades , Futures trades and Forex trades

class StockTrade(Trade):
    VALID_EXCHANGES = {'NYSE', 'NASDAQ', 'AMEX', 'CHX'}  # Example set of valid exchanges
    VALID_SIDES = {"buy", "sell"}

    def __init__(self, trade_id: str, exchange: str, symbol: str, price: Decimal, quantity: int, side: str):
        """
        Instead of this , Python can do Dictionary-based Dispatch and Mapping Conditions to Functions ValueError
        used to handle situations where the input is not appropriate for the expected type ,
        like InputMismatchException in Java

        The raise statement in Python is used to trigger an exception manually
        """
        if not trade_id:
            raise ValueError("Trade ID cannot be empty.")
        if exchange not in self.VALID_EXCHANGES:
            raise ValueError(f"Invalid exchange: {exchange}")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if side not in self.VALID_SIDES:
            raise ValueError(f"Invalid side: {side}. Must be 'buy' or 'sell'.")

        super().__init__(trade_id, exchange, symbol, price, quantity, side)

    """
        def validate_input(self, trade_id, exchange, symbol, price, quantity, side):
        errors = {
            "Trade ID": (not trade_id, "Trade ID cannot be empty."),
            "Exchange": (exchange not in self.VALID_EXCHANGES, f"Invalid exchange: {exchange}"),
            "Symbol": (not symbol, "Symbol cannot be empty."),
            "Price": (price <= 0, "Price must be greater than zero."),
            "Quantity": (quantity <= 0, "Quantity must be greater than zero."),
            "Side": (side not in self.VALID_SIDES, f"Invalid side: {side}. Must be 'buy' or 'sell'."),
        }

        for field, (condition, error_message) in errors.items():
            if condition:
                raise ValueError(f"{field} error: {error_message}")
    """

    def __str__(self):
        return (f"Trade ID: {self.trade_id}, "
                f"Symbol: {self.symbol}, "
                f"Price: {self.price}, "
                f"Quantity: {self.quantity}, "
                f"Side: {self.side}")

    def value(self) -> Decimal:
        return self.price * self.quantity

    # __lt__: Implements less than. (Object types)
    def __lt__(self, other):
        return self.value() < other.value()

    # __le__: Implements less than or equal to. (Object types)
    def __le__(self, other):
        return self.value() <= other.value()

    # __eq__: Implements equality. (Object types)
    def __eq__(self, other):
        return self.value() == other.value()

    # __ne__: Implements not equal to. (Object types)
    def __ne__(self, other):
        return self.value() != other.value()

    # __gt__: Implements greater than. (Object types)
    def __gt__(self, other):
        return self.value() > other.value()

    # __ge__: Implements greater than or equal to. (Object types)
    def __ge__(self, other):
        return self.value() >= other.value()

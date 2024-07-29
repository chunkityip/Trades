from decimal import Decimal
from trade import Trade

# This class can be Bond trades , Futures trades and Forex trades

class StockTrade(Trade):
    VALID_EXCHANGES = {"NYSE", "NASDAQ", "CHX"}  # Example set of valid exchanges
    VALID_SIDES = {"buy", "sell"}

    def __init__(self, trade_id: str, exchange: str, symbol: str, price: Decimal, quantity: int, side: str):
        """
        Instead of this , Python can do Dictionary-based Dispatch and Mapping Conditions to Functions ValueError
        used to handle situations where the input is not appropriate for the expected type ,
        like InputMismatchException in Java

        The raise statement in Python is used to trigger an exception manually

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
        """

        self.validate_input(trade_id, exchange, symbol, price, quantity, side)

        self.trade_id = trade_id
        self.exchange = exchange
        self.symbol = symbol
        self.price = price
        self.quantity = quantity
        self.side = side

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

    def value(self) -> Decimal:
        return self.price * self.quantity

    def __str__(self) -> str:
        return (f"Trade ID: {self.trade_id}, Symbol: {self.symbol}, Price: {self.price}, "
                f"Quantity: {self.quantity}, Side: {self.side}")
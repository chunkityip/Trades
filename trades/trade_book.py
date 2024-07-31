from decimal import Decimal
from typing import List
from .trade import Trade


class Tradebook:
    def __init__(self):
        self.trades: List[Trade] = []
        self.first_trade: Trade = None
        self.large_trades: List[Trade] = []
        self.small_trades: List[Trade] = []
        self.same_trades: List[Trade] = []

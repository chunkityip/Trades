from trades.stock_trade import StockTrade
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

    def add_trade(self, trade: StockTrade):
        self.trades.append(trade)
        # If it already has first trade
        if not self.first_trade:
            self.first_trade = trade
            self.same_trades.append(trade)
        else:
            self.categorize_trade(trade)

    """
    If the value of trade at first one larger than the first trade , go to large trades
    Else if the value of trade at first one smaller than the first trade , go to small trades
    else , go to same trade
    """

    def categorize_trade(self, trade: Trade):
        if trade.value() > self.first_trade.value():
            self.large_trades.append(trade)
        elif trade.value() < self.first_trade.value():
            (self.small_trades.append(trade))
        else:
            self.same_trades.append(trade)

    def summarize_trade_comparison(self):
        print(f"The reference trade is {self.first_trade}")
        print(f"The largest trade is {len(self.large_trades)}, "
              f"the smallest Trade is {len(self.small_trades)} , "
              f"the same trade is {len(self.same_trades)}")
        print(f"Average Value as Largest trade is {self.average_value(self.large_trades)}")
        print(f"Average Value as Smallest trade is {self.average_value(self.small_trades)}")
        print(f"Average Value as Same trade is {self.average_value(self.same_trades)}")

    def average_value(self, trades: List[Trade]) -> Decimal:
        if not trades:
            return Decimal(0)
        return sum(trade.value() for trade in trades) / len(trades)

    def summarize_total_trades(self):
        buy_value = sum(trade.value() for trade in self.trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in self.trades if trade.side == "sell")
        return {"Total Buy Value": buy_value, "Total Sell Value": sell_value}

    def summarize_by_symbol(self, symbol: str):
        filtered_trades = [trade for trade in self.trades if trade.symbol == symbol]
        buy_value = sum(trade.value() for trade in self.trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in self.trades if trade.side == "sell")
        return {"Symbol": symbol, "Total Buy Value": buy_value, "Total Sell Value": sell_value}

    def summarize_by_exchange(self, exchange: str):
        filtered_trades = filtered_trades = [trade for trade in self.trades if trade.exchange == exchange]
        buy_value = sum(trade.value() for trade in self.trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in self.trades if trade.side == "sell")
        return {"Exchange": exchange, "Total Buy Value": buy_value, "Total Sell Value": sell_value}


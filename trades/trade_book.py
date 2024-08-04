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

    def print_reference_trades_statistics(self):
        self.print_statistics(self.same_trades, "Reference Trades")

    def print_small_trades_statistics(self):
        self.print_statistics(self.small_trades, "Small Trades")

    def print_large_trades_statistics(self):
        self.print_statistics(self.large_trades, "Large Trades")

    def print_statistics(self, trades: List[Trade], trade_type: str):
        if not trades:
            print(f"No {trade_type}.")
            return

        total_value = sum(trade.value() for trade in trades)
        average_value = total_value / len(trades)
        print(f"{trade_type} Statistics:")
        print(f"Number of trades: {len(trades)}")
        print(f"Total value of trades: {total_value}")
        print(f"Average value of trades: {average_value}")

    def summarize_trade_comparison(self):
        if not self.trades:
            print("No trades to compare.")
            return

        self.large_trades.clear()
        self.small_trades.clear()
        self.same_trades.clear()

        for trade in self.trades:
            if trade != self.first_trade:
                self.categorize_trade(trade)

        print(f"The reference trade is {self.first_trade}")
        self.print_reference_trades_statistics()
        self.print_small_trades_statistics()
        self.print_large_trades_statistics()

    def average_value(self, trades: List[Trade]) -> Decimal:
        if not trades:
            return Decimal(0)
        return sum(trade.value() for trade in trades) / len(trades)

    # Total value of all trades for a given day
    def summarize_total_trades(self):
        buy_value = sum(trade.value() for trade in self.trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in self.trades if trade.side == "sell")
        return {"Total Buy Value": buy_value, "Total Sell Value": sell_value}

    # Total values for the trades with specific stock symbol
    def summarize_by_symbol(self, symbol: str):
        filtered_trades = [trade for trade in self.trades if trade.symbol == symbol]
        buy_value = sum(trade.value() for trade in filtered_trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in filtered_trades if trade.side == "sell")
        return {"Symbol": symbol, "Total Buy Value": buy_value, "Total Sell Value": sell_value}

    # Total values for the trades base ony exchange , such as NYSE, NASDAQ, CHX
    def summarize_by_exchange(self, exchange: str):
        filtered_trades = [trade for trade in self.trades if trade.exchange == exchange]
        buy_value = sum(trade.value() for trade in filtered_trades if trade.side == "buy")
        sell_value = sum(trade.value() for trade in filtered_trades if trade.side == "sell")
        return {"Exchange": exchange, "Total Buy Value": buy_value, "Total Sell Value": sell_value}


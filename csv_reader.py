import csv
from decimal import Decimal
from trades.stock_trade import StockTrade
from trades.trade_book import Tradebook


def read_trades_from_csv(file_path: str) -> Tradebook:
    tradebook = Tradebook()
    with open(file_path, mode="r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            time, exchange, symbol, quantity, price, side = row
            trade = StockTrade(
                trade_id=time,
                exchange=exchange,
                symbol=symbol,
                price=Decimal(price),
                quantity=int(quantity),
                side=side
            )
            tradebook.add_trade(trade)
        return tradebook


if __name__ == "__main__":
    tradebook = read_trades_from_csv("trades.csv")

    print("Summary of Total Trades:")
    print(tradebook.summarize_total_trades())

    symbol = input("Enter a stock symbol to summarize: ")
    print(tradebook.summarize_by_symbol(symbol))

    exchange = input("Enter an exchange to summarize: ")
    print(tradebook.summarize_by_exchange(exchange))

    tradebook.summarize_trade_comparison()

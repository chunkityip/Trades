import csv
from decimal import Decimal
from trades.stock import Stock  # Correct import path
from trades.trade_book import Tradebook


def read_trades_from_csv(file_path: str) -> Tradebook:
    tradebook = Tradebook()
    trade_id_counter = 1  # Initialize a counter for generating unique trade IDs
    with open(file_path, mode="r") as file:
        # Each element is separated by a semicolon(;).
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            time, exchange, symbol, quantity, price, side = row
            trade_id = f"id{trade_id_counter}"
            trade = Stock(
                trade_id=trade_id,
                exchange=exchange,
                symbol=symbol,
                price=Decimal(price),
                quantity=int(quantity),
                side=side
            )
            tradebook.add_trade(trade)
            trade_id_counter += 1
    return tradebook


if __name__ == "__main__":
    tradebook = read_trades_from_csv("trades/trades.csv")

    print("Summary of Total Trades:")
    print(tradebook.summarize_total_trades())
    print("---------------------------------")

    symbol = input("Enter a stock symbol to summarize: ")
    print(tradebook.summarize_by_symbol(symbol))
    print("---------------------------------")

    exchange = input("Enter an exchange to summarize: ")
    print(tradebook.summarize_by_exchange(exchange))
    print("---------------------------------")

    print("Here is the summary of trade comparison")
    tradebook.summarize_trade_comparison()

from trades.trade_book import Tradebook
from csv_reader import read_trades_from_csv

def main():
    # Read trades from CSV file
    tradebook = read_trades_from_csv("trades.csv")

    # Generate and print the statistics
    print("Total Trades Summary:", tradebook.summarize_total_trades())
    symbol = input("Enter a stock symbol to summarize: ").strip()
    print(f"Summary by Symbol ({symbol}):", tradebook.summarize_by_symbol(symbol))
    exchange = input("Enter an exchange name to summarize: ").strip()
    print(f"Summary by Exchange ({exchange}):", tradebook.summarize_by_exchange(exchange))

    # Trade comparison statistics
    tradebook.summarize_trade_comparison()

if __name__ == "__main__":
    main()


import csv
from decimal import Decimal
from trades.stock_trade import StockTrade


def read_trades_from_csv(file_path):
    trades = []
    with open(file_path, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        for row in csv_reader:
            try:
                trade = StockTrade(
                    trade_id=row[0],
                    exchange=row[1],
                    symbol=row[2],
                    price=Decimal(row[4]),
                    quantity=int(row[3]),
                    side=row[5]
                )
                trades.append(trade)
            except (ValueError, IndexError) as e:
                print(f"Skipping invalid row: {row} - {e}")
    return trades

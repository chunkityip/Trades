
from decimal import Decimal
from trades.stock_trade import StockTrade
from trades.trade_book import Tradebook

class driver():
    # Create stock trade instances
    stock1 = StockTrade("id1", "CHX", "FB", Decimal("100.00"), 120, "sell")
    print(stock1)
    stock2 = StockTrade("id2", "NASDAQ", "AAPL", Decimal("150.50"), 75, "buy")
    print(stock2)
    stock3 = StockTrade("id3", "CHX", "ORCL", Decimal("70.22"), 160, "sell")
    print(stock3)
    stock4 = StockTrade("id4", "NYSE", "F", Decimal("50.34"), 200, "buy")
    print(stock4)
    stock5 = StockTrade("id5", "NASDAQ", "AAPL", Decimal("155.99"), 65, "buy")
    print(stock5)
    stock6 = StockTrade("id6", "NASDAQ", "F", Decimal("55.12"), 200, "buy")
    print(stock6)
    stock7 = StockTrade("id7", "NYSE", "FB", Decimal("100.34"), 120, "sell")
    print(stock7)
    stock8 = StockTrade("id8", "CHX", "AAPL", Decimal("150.44"), 75, "buy")
    print(stock8)
    stock9 = StockTrade("id9", "NYSE", "AAPL", Decimal("150.73"), 80, "sell")
    print(stock9)
    stock10 = StockTrade("id10", "CHX", "ORCL", Decimal("75.89"), 170, "sell")
    print(stock10)


    # Create stock trade instances
    stock1 = StockTrade("id1", "CHX", "FB", Decimal("100.00"), 120, "sell")
    stock2 = StockTrade("id2", "NASDAQ", "AAPL", Decimal("150.50"), 75, "buy")
    stock3 = StockTrade("id3", "CHX", "ORCL", Decimal("70.22"), 160, "sell")
    stock4 = StockTrade("id4", "NYSE", "F", Decimal("50.34"), 200, "buy")
    stock5 = StockTrade("id5", "NASDAQ", "AAPL", Decimal("155.99"), 65, "buy")
    stock6 = StockTrade("id6", "NASDAQ", "F", Decimal("55.12"), 200, "buy")
    stock7 = StockTrade("id7", "NYSE", "FB", Decimal("100.34"), 120, "sell")
    stock8 = StockTrade("id8", "CHX", "AAPL", Decimal("150.44"), 75, "buy")
    stock9 = StockTrade("id9", "NYSE", "AAPL", Decimal("150.73"), 80, "sell")
    stock10 = StockTrade("id10", "CHX", "ORCL", Decimal("75.89"), 170, "sell")

    # Create Trade book and add trades
    tradebook = Tradebook()
    tradebook.add_trade(stock1)
    tradebook.add_trade(stock2)
    tradebook.add_trade(stock3)
    tradebook.add_trade(stock4)
    tradebook.add_trade(stock5)
    tradebook.add_trade(stock6)
    tradebook.add_trade(stock7)
    tradebook.add_trade(stock8)
    tradebook.add_trade(stock9)
    tradebook.add_trade(stock10)

    # Generate and print the statistics
    tradebook.print_reference_trades_statistics()
    tradebook.print_small_trades_statistics()
    tradebook.print_large_trades_statistics()

if __name__ == "__main__":
    driver()

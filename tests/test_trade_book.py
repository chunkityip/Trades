import pytest
from decimal import Decimal
from trades.stock_trade import StockTrade
from trades.trade_book import Tradebook
from unittest.mock import patch


@pytest.fixture
def tradebook():
    tb = Tradebook()
    tb.add_trade(StockTrade("id1", "CHX", "FB", Decimal("100.00"), 120, "sell"))
    tb.add_trade(StockTrade("id2", "NASDAQ", "AAPL", Decimal("150.50"), 75, "buy"))
    tb.add_trade(StockTrade("id3", "CHX", "ORCL", Decimal("70.22"), 160, "sell"))
    tb.add_trade(StockTrade("id4", "NYSE", "F", Decimal("50.34"), 200, "buy"))
    tb.add_trade(StockTrade("id5", "NASDAQ", "AAPL", Decimal("155.99"), 65, "buy"))
    tb.add_trade(StockTrade("id6", "NASDAQ", "F", Decimal("55.12"), 200, "buy"))
    tb.add_trade(StockTrade("id7", "NYSE", "FB", Decimal("100.34"), 120, "sell"))
    tb.add_trade(StockTrade("id8", "CHX", "AAPL", Decimal("150.44"), 75, "buy"))
    tb.add_trade(StockTrade("id9", "NYSE", "AAPL", Decimal("150.73"), 80, "sell"))
    tb.add_trade(StockTrade("id10", "CHX", "ORCL", Decimal("75.89"), 170, "sell"))
    return tb


@patch.object(Tradebook, 'print_statistics')
def test_print_reference_trades_statistics(mock_print_statistics, tradebook):
    tradebook.print_reference_trades_statistics()
    mock_print_statistics.assert_called_once_with(tradebook.same_trades, "Reference Trades")


@patch.object(Tradebook, 'print_statistics')
def test_print_small_trades_statistics(mock_print_statistics, tradebook):
    tradebook.print_small_trades_statistics()
    mock_print_statistics.assert_called_once_with(tradebook.small_trades, "Small Trades")


@patch.object(Tradebook, 'print_statistics')
def test_print_large_trades_statistics(mock_print_statistics, tradebook):
    tradebook.print_large_trades_statistics()
    mock_print_statistics.assert_called_once_with(tradebook.large_trades, "Large Trades")


@patch.object(Tradebook, 'print_statistics')
def test_summarize_trade_comparison(mock_print_statistics, tradebook):
    tradebook.summarize_trade_comparison()
    assert mock_print_statistics.call_count == 3
    mock_print_statistics.assert_any_call(tradebook.large_trades, "Large Trades")
    mock_print_statistics.assert_any_call(tradebook.small_trades, "Small Trades")
    mock_print_statistics.assert_any_call(tradebook.same_trades, "Reference Trades")


if __name__ == "__main__":
    tradebook()

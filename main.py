import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

"""
This script gets stock data, calculates the percentage change in stock price, 
and graphs the prices with a visual representation of the price movement.

Modules:
- yfinance
- matplotlib
- pandas
"""

def get_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data


def calculate_percentage_change(data):
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    percentage_change = ((end_price - start_price) / start_price) * 100
    return percentage_change


def show_stock_price(data, ticker,percentage_change):
    if data['Close'].iloc[-1] > data['Close'].iloc[0]:
        line_color = 'green'
    else:
        line_color = 'red' 
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    plt.plot(data.index, data['Close'], label=f"{ticker} Close Prices", color=line_color)
    plt.title(ticker + ' Stock Price')
    plt.xlabel('Date')
    plt.ylabel('Price ($USD)')
    plt.grid()
    plt.legend()
    plt.text(0.05, 0.95, f"Change: {percentage_change:.2f}%", 
             fontsize=12, verticalalignment='top', horizontalalignment='left',
             transform=plt.gca().transAxes)
    plt.show()

if __name__ == "__main__":
    ticker = input('Enter the stock ticker (e.g., AAPL, MSFT): ').upper()
    start_date = input('Enter the start date (YYYY-MM-DD): ')
    end_date = input('Enter the end date (YYYY-MM-DD): ')

    try:
        stock_data = get_stock_data(ticker, start_date, end_date)
        if stock_data.empty:
            print('No data found for ' + ticker + ' within the specified date range.')
        else:
            change = calculate_percentage_change(stock_data)
            show_stock_price(stock_data, ticker, change)
    except Exception as er:
        print(f"An error occurred: {er}")

import requests
import time
import pandas as pd

# Get the stock symbol from the user.
stock = input("Enter stock symbol: ")

# Get the API key from the user.
api_key = "......."

# Get the stock price.
def get_stock_price(stock_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={stock_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price

# Get the stock quote.
def get_stock_quote(stock_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={stock_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response

# Get the stock data.
stockdata = get_stock_quote(stock, api_key)
stock_price = get_stock_price(stock, api_key)

# Get the stock name, exchange, currency, open price, high price, low price, close price, and volume.
exchange = stockdata['exchange']
currency = stockdata['currency']
open_price = float(stockdata['open'])
high_price = float(stockdata['high'])
low_price = float(stockdata['low'])
close_price = float(stockdata['close'])
volume = stockdata['volume']
name = stockdata['name']

# Create a dictionary of the stock data.
data = {
    "Stock Name": name,
    "Stock Price": stock_price,
    "Exchange": exchange,
    "Currency": currency,
    "Open Price": round(open_price, 2),
    "High Price": round(high_price, 2),
    "Low Price": round(low_price, 2),
    "close price": round(close_price, 2),
    "Volume": volume,
}

# Define the columns variable.
columns = list(data.keys())

# Create the Pandas DataFrame.
df = pd.DataFrame(data, index=columns)

# Save the output as a CSV file.
df.to_csv("stock_quote.csv")

# Print each key-value pair in the stock_data dictionary on a new line.
def print_each_word_on_new_line(stock_data):
    for key, value in stock_data.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    stock_data = data
    print_each_word_on_new_line(stock_data)


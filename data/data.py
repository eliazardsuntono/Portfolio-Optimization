import yfinance as yf
import pandas as pd
import os

# Parameters
tickers = ['AAPL', 'TSLA', 'AMZN', 'NFLX']
start = '2024-01-01'
end = '2025-01-01'
file_path = 'data.csv'

if __name__ == '__main__':
    stock_data = {}

    for ticker in tickers:
        data = yf.download(ticker, start=start, end=end)
        stock_data[ticker] = data['Adj Close'] 

    df = pd.DataFrame(stock_data)
    
    df.to_csv(file_path, index=True)
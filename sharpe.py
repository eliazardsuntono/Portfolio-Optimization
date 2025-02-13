import pandas as pd
import numpy as np
import yfinance as yf

data_path = './data/data.csv'

def calculate_sharpe(tickers, data_path, risk_free_rate=0.03):
    # weights: Assume equal weight for each asset in the portfolio
    weights = [1 / len(tickers)] * len(tickers)   
    returns = {}
    
    for ticker in tickers:
        data = pd.read_csv(data_path)
        returns[ticker] = data[ticker].iloc[-1] / 100
    
    expected_returns = np.array([returns[ticker] for ticker in tickers])
    portfolio_return = np.dot(weights, expected_returns)
    
    std_dev = np.std(expected_returns)
    
    sharpe_ratio = (portfolio_return - risk_free_rate) / std_dev
    
    return sharpe_ratio, portfolio_return, std_dev

if __name__ == "__main__":
    tickers = ['AAPL', 'TSLA', 'AMZN', 'NFLX']
    data_path = './data/data.csv'
    risk_free_asset = yf.download("^TNX", period="1y")
    rf_rate = risk_free_asset["Close"].iloc[-1] / 100
    sharpe_ratio, portfolio_return, std_dev = calculate_sharpe(tickers, data_path, rf_rate)
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Portfolio Return: {portfolio_return:.2f}")
    print(f"Std. Deviation: {std_dev:.2f}")

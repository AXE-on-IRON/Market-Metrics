import pandas as pd
import numpy as np

def calculate_sma(prices, window=3):
    """Calculates the Simple Moving Average (SMA)."""
    if len(prices) < window:
        return []
    return pd.Series(prices).rolling(window=window).mean().dropna().tolist()

def calculate_volatility(prices):
    """Calculates the standard deviation of daily returns."""
    if len(prices) < 2:
        return 0.0
    returns = np.diff(prices) / prices[:-1]
    return np.std(returns)

if __name__ == "__main__":
    print("--- Market Metrics Engine Initialized ---")
    
    # Sample daily closing prices for demonstration
    sample_prices = [150.00, 152.50, 151.20, 155.00, 157.30, 156.10, 159.00]
    
    print(f"Sample Prices: {sample_prices}")
    
    sma_results = calculate_sma(sample_prices)
    print(f"3-Day SMA: {[round(val, 2) for val in sma_results]}")
    
    volatility = calculate_volatility(sample_prices)
    print(f"Estimated Volatility: {volatility:.4f}")

# imports - data and dates
import yfinance as yf
from datetime import datetime
import os

# Retrieving today's date
todayDate = datetime.today().strftime("%Y-%m-%d")
folderPath = "C:/Users/rohan/Coding/financewebsrape/companies-stock_data"


# Function defining to saving of stock data
def save_stock_data(ticker, nameFile):
    # Start date for data
    data = yf.download([ticker], start="2024-01-01")
    # Applies 'Date' as column for prediction.py
    data.reset_index(inplace=True)
    filename = f"{nameFile}.{todayDate}.csv"
    full_path = f"{folderPath}/{filename}"
    data.to_csv(full_path, index=False)
    print(f"Saved {full_path}")


# List of stock ticker and name
stocks = {
    "AAPL": "Apple",
    "MSFT": "Microsoft",
    "ABNB": "Airbnb",
    "AMZN": "Amazon",
    "GOOGL": "Google",
    "META": "Meta",
    "TGT": "Target",
    "WMT": "Walmart",
    "NVDA": "NVIDIA-Corp",
    "PLTR": "Palantir-Technologies-Inc",
    "JPM": "JPMorgan-Chase-&-Co",
    "NKE": "Nike-Inc",
    "COST": "Costco",
    # More to come
}

# Loop through each stock, saving ticker and name listed above
for ticker, name in stocks.items():
    save_stock_data(ticker, name)

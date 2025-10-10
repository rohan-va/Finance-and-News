# imports - data and dates
import yfinance as yf
from datetime import datetime
import os
import pandas as pd

# Retrieving today's date
folderPath = "C:/Users/rohan/Coding/financewebsrape/companies-stock_data"


# Function defining to saving of stock data
def save_stock_data(ticker, nameFile):
    # Start date for data
    todayDate = datetime.today().strftime("%Y-%m-%d")
    data = yf.download([ticker], start=todayDate, end=todayDate)

    # Applies 'Date' as column for prediction.py
    data.reset_index(inplace=True)

    filename = f"{nameFile}.{todayDate}.csv"
    full_path = os.path.join(folderPath, filename)

    data.to_csv(full_path, index=False)
    print(f"Saved {full_path}")

    # If file exists, append new data. Else, create new file
    if os.path.exists(full_path):
        existing = pd.read_csv(full_path)
        if todayDate in existing["Date"].values:
            print(f"{nameFile}: Data for {todayDate} already exists!")
            return
        updated = pd.concat([existing, data], ignore_index=False)
    else:
        updated = data
    updated.to_csv(full_path, index=False)
    print(f"{nameFile}: Updated {full_path}")


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
    "AVGO": "Broadcom",
    "2222.SR": "Saudi-Aramco",
    "TSM": "Taiwan-Semiconducter-Manufacturing",
    # More to come
}

# Loop through each stock, saving ticker and name listed above
for ticker, name in stocks.items():
    save_stock_data(ticker, name)

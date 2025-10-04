# imports - yfinance and datetime
import yfinance as yf
from datetime import datetime

# Retrieving today's date
todayDate = datetime.today().strftime("%Y-%m-%d")


# Function defining to saving of stock data
def save_stock_data(ticker, nameFile):
    # Start date for data
    data = yf.download([ticker], start="2024-01-01")
    # Applies 'Date' as column for prediction.py
    data.reset_index(inplace=True)
    filename = f"{nameFile}.{todayDate}.csv"
    data.to_csv(filename, index=False)
    print(f"Saved {filename}")


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
}

# Loop through each stock, saving ticker and name listed above
for ticker, name in stocks.items():
    save_stock_data(ticker, name)

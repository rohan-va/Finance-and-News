# imports
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# getting data from many stocks and creating csv's (order provided)
dataappl = yf.download(["AAPL"], start="2024-01-01")
dataappl.reset_index(inplace=True)
dataappl.to_csv("Apple.csv", index=False)

datamsft = yf.download(["MSFT"], start="2024-01-01")
datamsft.reset_index(inplace=True)
datamsft.to_csv("Microsoft.csv", index=False)

databnb = yf.download(["ABNB"], start="2024-01-01")
databnb.reset_index(inplace=True)
databnb.to_csv("Airbnb.csv", index=False)

dataamzn = yf.download(["AMZN"], start="2024-01-01")
dataamzn.reset_index(inplace=True)
dataamzn.to_csv("Amazon.csv", index=False)

datagoogl = yf.download(["GOOGL"], start="2024-01-01")
datagoogl.reset_index(inplace=True)
datagoogl.to_csv("Google.csv", index=False)

datameta = yf.download(["META"], start="2024-01-01")
datameta.reset_index(inplace=True)
datameta.to_csv("Meta.csv", index=False)

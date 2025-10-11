# Financial Webscraping and Model Predicting

This repository is dedicated for a python webscraper. This will consist files related to a scraper that will scrape data online from certain urls (Google Finance, Yahoo Finance, etc.) including stocks, close/open values, volume, etc. and predict them using a RandomForestClassifier model, displaying the predictions in a plot-based image.

Can be run after closing for a day to update stock close price and vary predictions.

More to come...👀

New additions ( After week of 9/28 )

- Added datetime import to update csv per new day/stock open
- Updated csv's path and download to specific folder in both .py files
- Included 'reports' folder for the results of RandomForest model. Consists of f1-score, accuracy, etc.
- Overriding of certain reports and plots depending on new information and if run multiple times per day

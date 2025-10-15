# Financial Webscraping and Model Predicting

This repository is dedicated for a python webscraper. This will consist files related to a scraper that will scrape data from Yahoo Finance including stocks, close/open values, volume, and more within. THen, another file is responsible for the prediction of said data using a RandomForestClassifier model, displaying the predictions in a plot-based image and producing reports per the model in .txt files.

Can be run after closing for a day to update stock close price and vary predictions.

More to come...👀

New additions ( After week of 9/28 )

- Added datetime import to update csv per new day/stock open
- Updated csv's path and download to specific folder in both .py files
- Included 'reports' folder for the results of RandomForest model. Consists of f1-score, accuracy, etc.
- Overriding of certain reports and plots depending on new information and if run multiple times per day

# News Webscraping
This is the news scrapper portion of the repository. This scraper attains past news articles over 24 hours spans alerting us about new information regarding stocks, finance, etc.

- 24-hour fetching
- CSV Updates based on each day
- Overrides information upon running
- Attain sources for a single source right now

#Areas to improve

- Need to include more news sources
- Gear towards specific stocks and coins to investigate certain trends
- Expand to a 7-day span

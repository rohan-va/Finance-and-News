import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import os


def process_stock_csvs(file_path, output_folder):
    company_name = os.path.splitext(os.path.basename(file_path))[0]
    df = pd.read_csv(
        file_path,
        parse_dates=["Date"],
        index_col="Date",
    )  # Read all dates in airbnb.csv
    df = df[["Close"]]  # Focus on the closing prices per day
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df.dropna(subset=["Close"], inplace=True)
    # Structure to help model
    df["SMA_5"] = df["Close"].rolling(window=5).mean()
    df["SMA_10"] = df["Close"].rolling(window=10).mean()
    df["Return"] = df["Close"].pct_change()

    # Give the model a target value (if went up = 1, else 0)
    df["Target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)

    # ML Model
    X = df[["SMA_5", "SMA_10", "Return"]]
    y = df["Target"]
    # Model Training

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.2
    )
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predicitons
    predictions = model.predict(X_test)
    print(f"\nResults for {os.path.basename(file_path)}")
    print(classification_report(y_test, predictions))

    # Visualize the predicitons from model using matplot
    df_test = df.iloc[-len(y_test) :].copy()
    df_test["Prediction"] = predictions
    plt.figure(figsize=(12, 6))
    plt.plot(df_test.index, df_test["Close"], label="Actual Price")
    plt.plot(
        df_test.index[df_test["Prediction"] == 1],
        df_test["Close"][df_test["Prediction"] == 1],
        "g^",
        label="Predicted Up",
    )
    plt.plot(
        df_test.index[df_test["Prediction"] == 0],
        df_test["Close"][df_test["Prediction"] == 0],
        "rv",
        label="Predicted Down",
    )
    plt.legend()
    plt.title(f"{company_name} Stock's Price Predictions")

    # Saving plot(s)
    output_path = os.path.join(output_folder, f"{company_name}_prediction-plot.png")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.show()
    plt.close()


# Folder Paths - Data and Plots
dataFolder = "C:/Users/rohan/Coding/financewebsrape-Mantis/companies-stock_data"
output_folder = "C:/Users/rohan/Coding/financewebsrape-Mantis/plots"

# If folder doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Runs
for filename in os.listdir(dataFolder):
    if filename.endswith(".csv"):
        full_path = os.path.join(dataFolder, filename)
        process_stock_csvs(full_path, output_folder)

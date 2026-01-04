import numpy as np

def add_features(df):
    df["return"] = np.log(df["Close"] / df["Close"].shift(1))
    df["volatility"] = df["return"].rolling(20).std()
    df["momentum"] = df["return"].rolling(10).mean()
    df["volume_change"] = df["Volume"].pct_change()

    df["ma_fast"] = df["Close"].rolling(10).mean()
    df["ma_slow"] = df["Close"].rolling(50).mean()
    df["trend"] = df["ma_fast"] - df["ma_slow"]

    df.dropna(inplace=True)
    return df

import yfinance as yf
from datetime import datetime

def load_data(symbol, start="2015-01-01", end=None):
    if end is None:
        end = datetime.today().strftime("%Y-%m-%d")

    df = yf.download(symbol, start=start, end=end)

    if hasattr(df.columns, "levels"):
        df.columns = df.columns.get_level_values(0)

    df.dropna(inplace=True)
    return df

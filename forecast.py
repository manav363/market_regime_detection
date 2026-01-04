import pandas as pd
import numpy as np

def summarize_market(df):
    summary = {}

    summary["Average Daily Return"] = df["return"].mean()
    summary["Average Volatility"] = df["volatility"].mean()
    summary["Current Regime"] = int(df["regime"].iloc[-1])

    last_60 = df.tail(60)
    summary["Recent Trend Strength"] = last_60["momentum"].mean()

    return summary


def forecast_one_year(df, predictor):
    future = []

    current_regime = int(df["regime"].iloc[-1])

    transition_counts = np.zeros((4,4))

    for i in range(len(df)-1):
        transition_counts[df["regime"].iloc[i], df["regime"].iloc[i+1]] += 1

    transition_matrix = transition_counts / transition_counts.sum(axis=1, keepdims=True)

    for _ in range(252):
        probs = transition_matrix[current_regime]
        next_regime = np.random.choice([0,1,2,3], p=probs)
        future.append(next_regime)
        current_regime = next_regime

    return future

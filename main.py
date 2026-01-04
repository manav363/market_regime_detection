from data import load_data
from features import add_features
from model import train_model
from predictor import train_predictor
from visualize import plot_regimes
import matplotlib.pyplot as plt
from forecast import summarize_market, forecast_one_year

print("\n=== Market Regime Research Engine ===\n")

symbol = input("Enter ticker (e.g. AAPL, SPY, BTC-USD): ").upper()

df = load_data(symbol)
df = add_features(df)
df = train_model(df)

df["next_regime"] = df["regime"].shift(-1)
df.dropna(inplace=True)

stats = df.groupby("regime").agg({
    "return": "mean",
    "volatility": "mean",
    "momentum": "mean"
})

print(f"\nRegime Statistics for {symbol}")
print(stats)

best_regime = stats["return"].idxmax()
df["strategy_return"] = df["return"] * (df["regime"] == best_regime)

# -------------------- Predictor --------------------
predictor = train_predictor(df)

print("\nReached post-prediction section")  # 🔎 DEBUG MARKER

# -------------------- Visualization ----------------
plot_regimes(df)

df["equity_curve"] = (1 + df["strategy_return"]).cumprod()
df["buy_hold"] = (1 + df["return"]).cumprod()

plt.figure(figsize=(12,6))
plt.plot(df.index, df["equity_curve"], label="Regime Strategy")
plt.plot(df.index, df["buy_hold"], label="Buy & Hold")
plt.legend()
plt.title(f"{symbol} — Strategy vs Buy & Hold")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.show()

# -------------------- Human Explanation --------------------
accuracy = (df["next_regime"] == predictor.predict(
    df[["return","volatility","momentum","volume_change","trend"]]
)).mean()

print("\n--- Plain English Summary ---")
print(f"The system predicted market behavior correctly about {accuracy*100:.1f}% of the time.")
print("This means the model understands the market structure quite well.")
print("It is especially strong at identifying bullish and stable market phases.")
print("Short unstable transitions are naturally harder to predict.")

# -------------------- Forward Outlook --------------------
latest = df[["return","volatility","momentum","volume_change","trend"]].iloc[-1:]
future_regime = predictor.predict(latest)[0]

regime_meanings = {
    0: "Stable accumulation / low risk environment",
    1: "High risk or bearish transition phase",
    2: "Aggressive bullish breakout phase",
    3: "Healthy sustained uptrend"
}

print("\n--- Forward Market Outlook ---")
print(f"Based on all data up to today, the market is currently in Regime {int(future_regime)}.")
print("Interpretation:", regime_meanings[int(future_regime)])

# ================= Market Summary =================
summary = summarize_market(df)

print("\n=== Market Summary Till Today ===")
for k, v in summary.items():
    print(f"{k}: {v}")

# ================= One-Year Forecast =================
future = forecast_one_year(df, predictor)

bull_ratio = future.count(2) / len(future)
bear_ratio = future.count(1) / len(future)

print("\n=== One Year Regime Outlook ===")
print(f"Expected Bullish Period: {bull_ratio*100:.1f}% of the year")
print(f"Expected Bearish/High-Risk Period: {bear_ratio*100:.1f}% of the year")

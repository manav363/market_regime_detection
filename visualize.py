import matplotlib.pyplot as plt

def plot_regimes(df):
    plt.figure(figsize=(14,7))
    plt.plot(df.index, df["Close"], color="black", linewidth=1)

    for r in sorted(df["regime"].unique()):
        plt.scatter(
            df[df["regime"] == r].index,
            df[df["regime"] == r]["Close"],
            label=f"Regime {r}",
            s=10
        )

    plt.legend()
    plt.title("Market Regime Detection")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

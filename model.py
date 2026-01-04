from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def train_model(df, n_clusters=4):
    features = df[["return", "volatility", "momentum", "volume_change", "trend"]]

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df["regime"] = model.fit_predict(X)

    return df

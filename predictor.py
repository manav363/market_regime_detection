from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_predictor(df):
    X = df[["return", "volatility", "momentum", "volume_change", "trend"]]
    y = df["next_regime"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.2
    )

    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    print("\nRegime Prediction Report:\n")
    print(classification_report(y_test, preds))

    # ❗ DO NOT EXIT, DO NOT RETURN EARLY
    return model

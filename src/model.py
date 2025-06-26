from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


def train_model(df):
    print("\n---------------------Train phase-------------------------")

    X = df.drop("infested", axis=1).values
    y = df["infested"].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    model = Sequential(
        [
            Dense(64, input_dim=X_train.shape[1], activation="relu"),
            Dense(32, activation="relu"),
            Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"]
    )

    history = model.fit(
        X_train,
        y_train,
        epochs=10,
        batch_size=32,
        validation_data=(X_test, y_test),
    )

    model.save("models/malware_model.keras")

    y_pred_proba = model.predict(X_scaled).flatten()

    return (history, model, y_pred_proba)

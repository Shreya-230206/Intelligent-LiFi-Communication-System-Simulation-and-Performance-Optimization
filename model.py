import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("dataset.csv")

# Features (inputs)
X = df[["distance", "noise", "users"]]

# Targets (outputs)
y_throughput = df["throughput"]
y_latency = df["latency"]
y_packet_loss = df["packet_loss"]


# -----------------------------
# Train models (one for each metric)
# -----------------------------
def train_model(y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    error = mean_absolute_error(y_test, preds)

    return model, error


# Train all models
model_throughput, err_t = train_model(y_throughput)
model_latency, err_l = train_model(y_latency)
model_loss, err_p = train_model(y_packet_loss)


# -----------------------------
# Print model performance
# -----------------------------
print("Model Errors:")
print(f"Throughput MAE: {err_t:.2f}")
print(f"Latency MAE: {err_l:.2f}")
print(f"Packet Loss MAE: {err_p:.4f}")


# -----------------------------
# Prediction Example
# -----------------------------
def predict(distance, noise, users):
    input_data = [[distance, noise, users]]

    t = model_throughput.predict(input_data)[0]
    l = model_latency.predict(input_data)[0]
    p = model_loss.predict(input_data)[0]

    return t, l, p


# Test prediction
print("\nSample Prediction:")
t, l, p = predict(5, 0.1, 3)

print(f"Throughput: {t:.2f}")
print(f"Latency: {l:.2f}")
print(f"Packet Loss: {p:.4f}")


# -----------------------------
# Optimization (Best conditions)
# -----------------------------
best = None
best_score = -1

for d in range(1, 11):
    for n in [0.05, 0.1, 0.2, 0.3]:
        for u in range(1, 11):
            t, l, p = predict(d, n, u)

            score = t - l  # maximize throughput, minimize latency

            if score > best_score:
                best_score = score
                best = (d, n, u, t, l, p)

print("\nBest Conditions Found:")
print(f"Distance: {best[0]} m")
print(f"Noise: {best[1]}")
print(f"Users: {best[2]}")
print(f"Throughput: {best[3]:.2f}")
print(f"Latency: {best[4]:.2f}")
print(f"Packet Loss: {best[5]:.4f}")

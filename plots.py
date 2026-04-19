import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("dataset.csv")


# -----------------------------
# Plot 1: Throughput vs Distance
# -----------------------------
plt.figure()
plt.scatter(df["distance"], df["throughput"])
plt.xlabel("Distance (m)")
plt.ylabel("Throughput")
plt.title("Throughput vs Distance")
plt.savefig("throughput_vs_distance.png")
plt.close()


# -----------------------------
# Plot 2: Latency vs Users
# -----------------------------
plt.figure()
plt.scatter(df["users"], df["latency"])
plt.xlabel("Number of Users")
plt.ylabel("Latency")
plt.title("Latency vs Users")
plt.savefig("latency_vs_users.png")
plt.close()


# -----------------------------
# Plot 3: Packet Loss vs Noise
# -----------------------------
plt.figure()
plt.scatter(df["noise"], df["packet_loss"])
plt.xlabel("Noise")
plt.ylabel("Packet Loss")
plt.title("Packet Loss vs Noise")
plt.savefig("packet_loss_vs_noise.png")
plt.close()


print("Plots generated and saved as images.")

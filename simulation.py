import random
import csv

# -----------------------------
# LiFi Transmitter (LED logic)
# -----------------------------
def transmit(data):
    signal = []
    for bit in data:
        if bit == '1':
            signal.append(1)  # LED ON
        else:
            signal.append(0)  # LED OFF
    return signal


# -----------------------------
# LiFi Receiver (with noise)
# -----------------------------
def receive(signal, noise):
    received = ""
    for bit in signal:
        if random.random() < noise:
            bit = 1 - bit  # flip bit due to noise
        received += str(bit)
    return received


# -----------------------------
# Generate random binary data
# -----------------------------
def generate_data(length=16):
    return ''.join(random.choice(['0', '1']) for _ in range(length))


# -----------------------------
# Calculate performance metrics
# -----------------------------
def calculate_metrics(sent, received, distance, users):
    errors = sum(1 for a, b in zip(sent, received) if a != b)
    ber = errors / len(sent)

    throughput = max(0, 100 - (distance * 5 + ber * 100 + users * 3))
    latency = distance * 2 + users * 1.5 + ber * 50
    packet_loss = ber

    return throughput, latency, packet_loss


# -----------------------------
# Main simulation function
# -----------------------------
def simulate():
    # Random environment conditions
    distance = random.uniform(1, 10)   # meters
    noise = random.uniform(0, 0.3)     # noise level
    users = random.randint(1, 10)      # number of users

    # Generate and transmit data
    data = generate_data()
    signal = transmit(data)
    received = receive(signal, noise)

    # Calculate performance
    throughput, latency, packet_loss = calculate_metrics(
        data, received, distance, users
    )

    return [distance, noise, users, throughput, latency, packet_loss]


# -----------------------------
# Generate dataset
# -----------------------------
def generate_dataset(samples=2000):
    data = []

    for _ in range(samples):
        data.append(simulate())

    with open("dataset.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "distance",
            "noise",
            "users",
            "throughput",
            "latency",
            "packet_loss"
        ])
        writer.writerows(data)

    print("Dataset generated: dataset.csv")


# -----------------------------
# Run file
# -----------------------------
if __name__ == "__main__":
    generate_dataset()

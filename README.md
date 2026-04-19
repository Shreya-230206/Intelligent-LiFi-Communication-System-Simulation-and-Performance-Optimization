# Intelligent LiFi Communication System: Simulation and Performance Optimization

## Overview
This project presents a simulation-based LiFi (Light Fidelity) communication system that models data transmission using light signals and evaluates system performance under varying environmental conditions. By integrating machine learning techniques, the system predicts and optimizes key performance metrics such as throughput, latency, and packet loss.

---

## Abstract
LiFi (Light Fidelity) is an emerging optical wireless communication technology that enables high-speed data transmission using visible light. However, system performance is highly dependent on environmental factors such as distance, noise, and user load.

This project develops a simulation framework for a LiFi-based communication system, where binary data is transmitted using LED-based signaling and received with noise interference. The system evaluates performance metrics including throughput, latency, and packet loss under varying conditions.

A machine learning model is trained on the generated dataset to predict system performance and identify optimal configurations for improved efficiency. Results demonstrate that data-driven optimization significantly enhances system reliability and communication efficiency.

This project provides a scalable and flexible foundation for future research in optical wireless communication and intelligent network optimization.

---

## System Architecture
- LiFi Transmitter (LED-based binary signal simulation)
- LiFi Receiver (noise-affected signal decoding)
- Performance Evaluation Module
- Machine Learning Model for prediction and optimization

---

## Features
- Simulation of LiFi-based data transmission  
- Noise-aware communication modeling  
- Performance evaluation using:
  - Throughput  
  - Latency  
  - Packet Loss  
- Machine learning-based performance prediction  
- Data-driven optimization of system parameters  

---

## Technologies Used
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Scikit-learn  

---

## Implementation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/intelligent-lifi-communication-system.git
cd intelligent-lifi-communication-system
```
### 2. Install Dependencies
```bash
pip install numpy pandas matplotlib scikit-learn
```
### 3. Run Simulation
```bash
python simulation.py
```
Generates dataset (dataset.csv)
### 4. Generate Performance Plots
```bash
python plots.py
```
Creates visualization graphs
### 5. Train Machine Learning Model
```bash
python model.py
```
Predicts performance and finds optimal conditions


## Working Principle

### 1. LiFi Signal Modeling
The system models LiFi communication by encoding binary data into optical signals, where logical ‘1’ and ‘0’ are represented by LED ON/OFF states. This abstraction simulates intensity modulation used in real optical wireless communication systems.

---

### 2. Channel Impairment Simulation
The transmission channel is modeled to incorporate realistic impairments:
- **Distance-dependent attenuation** affecting signal strength  
- **Noise-induced bit errors** simulating environmental interference  
- **User load variation** representing network congestion  

These factors directly influence the reliability and efficiency of data transmission.

---

### 3. Receiver-Side Decoding and Error Analysis
The receiver reconstructs the transmitted bitstream under noisy conditions. Bit discrepancies between transmitted and received data are quantified using **Bit Error Rate (BER)**, which serves as the basis for evaluating packet loss and transmission reliability.

---

### 4. Performance Metric Computation
System performance is evaluated using:
- **Throughput** → Effective successful data delivery rate  
- **Latency** → Transmission delay influenced by load and channel conditions  
- **Packet Loss** → Derived from BER, indicating communication reliability  

These metrics provide a comprehensive view of system behavior under varying conditions.

---

### 5. Machine Learning-Based System Modeling
A supervised learning model (Random Forest Regressor) is trained on simulated data to learn the relationship between input parameters (distance, noise, users) and performance metrics.

---

### 6. Data-Driven Optimization
The trained model is used to:
- Predict system performance for unseen conditions  
- Identify optimal parameter configurations that maximize throughput and minimize latency  
- Enable intelligent adaptation of system behavior based on environmental conditions  

This transforms the system from a static simulation into an **intelligent, self-optimizing communication model**.

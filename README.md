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
### Data Transmission
- Binary data is transmitted using simulated LED signals 
- Receiver decodes signals with noise interference
### Performance Evaluation
- Throughput → data efficiency
- Latency → delay
- Packet Loss → error rate
### Machine Learning Optimization
- Uses Random Forest model
- Predicts system performance
- Finds optimal system configurations

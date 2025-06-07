# 🛡️ Smart DDoS Detection System

An intelligent DDoS detection and prevention system built using Python, Scapy, and basic ML concepts. Designed to monitor network traffic in real time, detect anomalies, and prevent potential Distributed Denial-of-Service (DDoS) attacks effectively.

---

## 🚀 Features

- 📡 Real-time packet sniffing and logging
- 🧠 Simple ML logic for anomaly detection
- 🔐 Automatic alerting and blocking based on thresholds
- 📊 Visualization-ready logs for future analysis
- 🧪 Simulated DDoS attack script for testing
- 🌐 Flask-based web dashboard (optional upgrade)

---

## 🧠 Concept

This tool monitors traffic flow (like SYN packets or ICMP floods) to detect traffic spikes. It identifies suspicious activity based on customizable thresholds (like packets/sec per IP) and triggers alerts or automated blocking.

---

## 🛠️ Tech Stack

- Python 3
- Scapy (packet sniffing)
- Pandas (logging & analysis)
- Matplotlib (optional plotting)
- Flask (for dashboard - WIP)

---

## 📁 Project Structure

📂 ddos-detector/
├── ddos_logs.csv # Logged packet data
├── simulate_ddos.py # Simulates an ICMP flood attack
├── smart_ddos_detector.py # Main detection script
├── requirements.txt # Dependencies


---

## ⚙️ Installation

1. Clone the repository:

git clone https://github.com/krishnaakshath/ddos-detector.git
cd ddos-detector

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt


▶️ Usage
To start the detector:
sudo python3 smart_ddos_detector.py

To simulate a DDoS attack (for testing):
sudo python3 simulate_ddos.py

📌 Note

    Make sure you run with sudo since Scapy needs root privileges.

    This project is for educational and research purposes only.

    Works best in a controlled lab or VM environment.

🧠 Future Scope

    📊 Web-based dashboard (Flask + Charts)

    🧠 ML model training on real traffic datasets

    🧱 Integration with iptables for auto-blocking

    📡 IDS + IPS hybrid model

🤝 Contributing

Pull requests are welcome! If you want to add features, fix bugs, or improve performance, feel free to fork and submit a PR.
📜 License

MIT License
🧑‍💻 Author

Kasibhatta Krishna Akshath
4th Year CS @ Andhra University
🔒 Cybersecurity Enthusiast | 🧠 ML Learner | 🛠️ Project Builder
📫 Email me

    ⚠️ Educational Use Only — Do not use for unethical hacking or unauthorized access. Always get permission before scanning or simulating attacks.

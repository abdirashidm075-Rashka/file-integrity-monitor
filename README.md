# Endpoint Security: File Integrity Monitor (FIM)

## 📝 Description
This endpoint defense tool mimics corporate File Integrity Monitoring (FIM) software. It is designed to track file system properties, establishing a cryptographic signature baseline of critical target assets using the **SHA-256 algorithm**. The script continuously checks the target files and throws immediate high-severity alerts if any operational modifications or administrative drift are detected.

## 🛠️ Features
* **Cryptographic Baselines:** Records authoritative hash footprints of target binaries or system configuration profiles.
* **Tamper Detection Engine:** Evaluates running check matches to capture real-time tampering signatures.
* **Incident Alerts:** Instantly broadcasts data discrepancy flags to assist security analyst triage.

## 🚀 How to Run It

### Prerequisites
* Python 3.x installed.

### Execution
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/file-integrity-monitor.git](https://github.com/YOUR-USERNAME/file-integrity-monitor.git)

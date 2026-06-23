# Basic Host-Based Intrusion Detection System (HIDS)

A lightweight, Python-based Intrusion Detection System (IDS) designed to monitor server authentication logs and automatically detect potential brute-force attacks. 

This project demonstrates core cybersecurity concepts, including log analysis, threat detection, and pattern recognition using regular expressions (Regex).

## 🚀 Features

* **Log Parsing:** Extracts actionable data from unstructured server logs (SSH, FTP, Web).
* **Threat Detection:** Automatically flags IP addresses that exceed a safe threshold of failed login attempts.
* **Regex Integration:** Utilizes Python's `re` module to accurately identify IPv4 addresses within varied log entry formats.
* **Categorized Alerting:** Differentiates between low-level warnings and critical brute-force attack alerts based on threat severity.

## 🛠️ Prerequisites

This script runs on standard Python. No external libraries or complex environments are required.
* Python 3.x


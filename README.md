# Security Automation & Enrichment Dashboard 🛡️

## Overview
Alert fatigue is a critical bottleneck in modern Security Operations Centers (SOC). This custom-built web application streamlines the Tier 1 Incident Response triage workflow. By automating the ingestion and enrichment of Indicators of Compromise (IOCs), analysts can instantly query external Threat Intelligence platforms and view actionable data within a unified, analyst-friendly dashboard.

<img width="1914" height="1081" alt="soc-automation-dashboard" src="https://github.com/user-attachments/assets/ac0a7b66-adb8-4529-b18a-0ab01ac1f958" />


## System Architecture (The 4 Core Pillars)
This tool bridges application development with incident response, built on an n-tier web architecture using **Python** and **Django**:

1. **The Frontend (UI/UX):** A custom HTML/CSS dark-mode interface designed for rapid data scanning. It features responsive text-wrapping to safely handle 64-character cryptographic hashes without layout distortion.
2. **The Controller (Routing):** The `views.py` engine automatically detects the payload type. If the user inputs an IPv4 address (containing a `.`), it routes to the IP analysis engine. If it detects an alphanumeric string without periods, it routes to the Hash analysis engine.
3. **The Engine (API Integration):** The `utils.py` module handles asynchronous HTTP requests. It securely fetches authentication keys via `python-dotenv`, queries the selected REST API, and parses the nested JSON response to extract only high-value analyst metrics.
4. **The Presentation (Dynamic Rendering):** Django's template tags dynamically structure the HTML payload, shifting the visual layout entirely based on whether network telemetry or malware engine detections are returned.

## Integrations
* **AbuseIPDB API:** Extracts Malicious Confidence Scores and Origin Country for IP addresses.
* **VirusTotal v3 API:** Performs multi-engine malware scanning for file hashes (MD5, SHA-1, SHA-256), returning specific malicious/suspicious detection counts and file type details.

## Setup and Installation
To run this tool locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Anugrahkv/soc-automation-dashboard.git](https://github.com/Anugrahkv/soc-automation-dashboard.git)
   cd soc-automation-dashboard

2. **Create and activate a virtual environment:**
   ```bash
    python -m venv env
    # On Windows:
    env\Scripts\activate
    # On macOS/Linux:
    source env/bin/activate

3. **Install dependencies:**
   ```bash
   pip install django requests python-dotenv

4. **Configure Environment Variables:**
    Create a .env file in the root directory. Do not commit this file to Git. Add your API keys:
    ```bash
    ABUSEIPDB_API_KEY=your_abuseipdb_key_here
    VIRUSTOTAL_API_KEY=your_virustotal_key_here

5. **Run the server:**
    ```bash
    python manage.py runserver

Navigate to http://127.0.0.1:8000/automation/ in your browser.

**Formal Project Documentation**
For a deep dive into the methodology, technical challenges overcome (including OS execution policy bypasses), and the future roadmap for this tool, please review the attached formal documentation: 
[SOC DASHBOARD REPORT.pdf](https://github.com/user-attachments/files/28952503/SOC.DASHBOARD.REPORT.pdf)



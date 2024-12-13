# Server Performance Monitoring and Alert System

## Project Overview

This project implements a simple monitoring system to track server performance metrics such as CPU usage, memory usage, and disk space. It triggers email alerts when usage exceeds predefined thresholds and logs metrics for analysis.

---

## Features

- **Monitor Server Metrics:** Tracks CPU, memory, and disk usage.
- **Threshold Alerts:** Sends email notifications for high resource usage.
- **Logging:** Records metrics in a log file for analysis.
- **Optional Visualization:** Displays metrics using a simple dashboard.

---

## Tools and Technologies

- **Programming Language:** Python
- **Libraries:**
  - `psutil`: For accessing system metrics
  - `smtplib`: For sending email alerts
  - `csv`: For logging data
  - (Optional) `Flask` or `Streamlit`: For real-time dashboard visualization

---

## Installation and Setup

1.  **Clone the Repository:**

    ```bash
    git clonehttps://github.com/oshadha2k01/server-monitoring-system.git
    cd server-monitoring-system
    ```

2.  **Create a Virtual Environment (Optional):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate   # Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Email Settings:**

    - Open `config.py` and set up your email credentials:
      ```python
      EMAIL_SENDER = "sender_example@gmail.com"
      EMAIL_PASSWORD = "email_password"
      EMAIL_RECEIVER = "receiver_example@gmail.com"

           ```

---

## Usage

1. **Run the Monitoring Script:**

   ```bash
   python monitor.py
   ```

2. **Check Logs:**
   Metrics are logged in `metrics_log.csv`.

3. **Optional Visualization:**
   Run the dashboard (if implemented) using Streamlit:
   ```bash
   streamlit run dashboard.py
   ```

---

## Future Enhancements

- Add real-time alerts via SMS or Slack.
- Integrate advanced visualization tools.
- Implement machine learning for anomaly detection.

---

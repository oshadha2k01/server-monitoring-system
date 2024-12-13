import psutil
import smtplib
import csv
from time import sleep
from datetime import datetime
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

# Thresholds
CPU_THRESHOLD = 80  # in %
MEMORY_THRESHOLD = 80  # in %
DISK_THRESHOLD = 80  # in %

# Log File
LOG_FILE = "metrics_log.csv"

def initialize_log():
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU (%)", "Memory (%)", "Disk (%)"])

def log_metrics(cpu, memory, disk):
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), cpu, memory, disk])

def send_alert(metric, value):
    subject = f"Alert: High {metric} Usage"
    body = f"{metric} usage is at {value}%. Please take action."
    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)
        print(f"Alert sent for {metric} usage.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def monitor():
    initialize_log()
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        print(f"CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%")
        log_metrics(cpu_usage, memory_usage, disk_usage)

        if cpu_usage > CPU_THRESHOLD:
            send_alert("CPU", cpu_usage)
        if memory_usage > MEMORY_THRESHOLD:
            send_alert("Memory", memory_usage)
        if disk_usage > DISK_THRESHOLD:
            send_alert("Disk", disk_usage)

        sleep(5)

if __name__ == "__main__":
    monitor()

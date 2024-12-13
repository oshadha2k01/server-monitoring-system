import os
import pandas as pd
import streamlit as st
from datetime import datetime
import csv

LOG_FILE = "metrics_log.csv"

# Initialize the log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "CPU (%)", "Memory (%)", "Disk (%)"])

def load_data():
    return pd.read_csv(LOG_FILE)

data = load_data()
st.title("Server Performance Monitoring Dashboard")
st.line_chart(data.set_index("Timestamp"))

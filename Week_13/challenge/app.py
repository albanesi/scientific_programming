from flask import Flask, render_template
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
import threading
import time
from datetime import datetime

app = Flask(__name__, template_folder='.')

# Current datetime
dt = datetime.now().strftime('%Y-%m-%d')

# Data frame
df = pd.DataFrame()

# Update data
def update_data():
    from water_level_data import hydro_data
    global df
    while True:
        hydro_data()
        df = pd.read_csv('hydro_data.csv', sep=';')
        time.sleep(10) # refresh every 10 seconds

# Create bar chart
@app.route('/')
def index():
    # Create bar chart
    data = df['drain'][-10:]
    labels = df['hour'][-10:]
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.bar(labels, data, color="greenyellow")
    ax.set_xlabel('time', fontsize=10)
    ax.set_ylabel('drainage (m3/s)', fontsize=10)
    ax.set_title(f'Drainage at {dt}', fontsize=12)
    plt.xticks(fontsize=9, rotation=0)
    plt.yticks(fontsize=9)
    ax.grid()

    # Save the plot to a .png image in memory
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    # Encode the plot image in base64
    bar_plot = base64.b64encode(img.getvalue()).decode()

    # Create line chart
    data = df['waterlevel'][-10:]
    labels = df['hour'][-10:]
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(labels, data, color="steelblue", marker='o')
    ax.set_xlabel('Time', fontsize=10)
    ax.set_ylabel('Water level (cm)', fontsize=10)
    ax.set_title(f'Water level at {dt}', fontsize=12)
    plt.xticks(fontsize=9, rotation=0)
    plt.yticks(fontsize=9)
    ax.grid()

    # Save the plot to a .png image in memory
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)

    # Encode the plot image in base64
    line_plot = base64.b64encode(img.getvalue()).decode()

    # Render the HTML template with the plot data
    return render_template('index.html', bar_plot=bar_plot, line_plot=line_plot)

# Update website
@app.route('/refresh')
def refresh():
    return render_template('index.html')

if __name__ == '__main__':
    # Start the data update thread
    data_thread = threading.Thread(target=update_data)
    data_thread.daemon = True
    data_thread.start()

    # Run the Flask app
    app.run()

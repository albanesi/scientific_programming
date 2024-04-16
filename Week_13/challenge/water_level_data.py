import os
import re
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

# Function
def hydro_data():

    try:

        # Current datetime and hour
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hr = datetime.now().strftime('%H:%M:%S')

        # Request website with hydrodata
        url = "https://pegelalarm.at/de/river.php?river=Thur"
        page = requests.get(url)

        # HTML-Parser
        soup = BeautifulSoup(page.content, "html.parser")

        # Extracting the data
        data = []
        for row in soup.find_all('tr'):
            row_data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            data.append(row_data)

        # Define column names
        columns = ['location', 'river', 'waterlevel_raw', 'drain_raw', 'link']

        # Create a DataFrame
        df = pd.DataFrame(data, columns=columns)

        # Numerical data 
        df['waterlevel'] = df['waterlevel_raw'].str.extract(r'([\d.]+)').astype(float)
        df['drain'] = df['drain_raw'].str.extract(r'([\d.]+)').astype(float)

        # Select station and columns
        df = df.loc[df['location'] == 'Andelfingen'].iloc[:,[0,1,5,6]]

        # Insert datetime and hour
        df.insert(0, 'datetime', dt)
        df.insert(1, 'hour', hr)

        # Save data to file
        # Path on Windows with filename
        filename = 'hydro_data.csv'
        # Path on Linux-Server with filename
        # filename = '/home/ubuntu/data/hydro_data.csv'

        # Check if file exists ...
        if not os.path.isfile('hydro_data.csv'):
            # Create file
            df.to_csv('hydro_data.csv', 
                    sep=";", 
                    encoding='utf-8',
                    index=False)
        else:
            # Append new data
            df.to_csv('hydro_data.csv', 
                    sep=";", 
                    encoding='utf-8', 
                    header=False,
                    index=False,
                    mode='a')
            
    except:
        pass

# Function call
hydro_data()
import requests
import json
import pandas as pd

username=''
password=''
UA142_icao='a2061e'
UA142_begin='1742806800' # March 23, 2025
UA142_end='1744646400'

UA142_url_tracking = f"https://{username}:{password}@opensky-network.org/api/tracks/all?icao24={UA142_icao}&time=0"

UA142_response = requests.get(UA142_url_tracking).json()
# UA142_response.raise_for_status()

# col_names = list(response[0].keys())
print(UA142_response)
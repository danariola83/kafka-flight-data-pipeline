import requests
import json
import pandas as pd

username=''
password=''
manila_icao='RPLL'
begin='1742659200' # March 23, 2025
end='1742918400'

manila_arrivals_url = f"https://{username}:{password}@opensky-network.org/api/flights/arrival?airport={manila_icao}&begin={begin}&end={end}"
manila_departures_url = f"https://{username}:{password}@opensky-network.org/api/flights/departure?airport={manila_icao}&begin={begin}&end={end}"

arrivals_response = requests.get(manila_arrivals_url).json()
departures_response = requests.get(manila_departures_url).json()
# UA142_response.raise_for_status()

# col_names = list(response[0].keys())
print(arrivals_response)
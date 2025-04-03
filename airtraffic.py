import requests
import json
import pandas as pd
import datetime

class AirTraffic:
    def __init__(self, lon_min, lat_min, lon_max, lat_max, user_name, password, country):
        self.lon_min = lon_min
        self.lat_min = lat_min
        self.lon_max = lon_max
        self.lat_max = lat_max
        self.user_name = user_name
        self.password = password
        self.country = country

    def get_flight_data(self):

        final_url = f"https://{self.user_name}:{self.password}@opensky-network.org/api/states/all?lamin={str(self.lat_min)}&lomin={str(self.lon_min)}&lamax={str(self.lat_max)}&lomax={str(self.lon_max)}&extended=1"

        response = requests.get(final_url)

        if response.status_code != 204:
            return response.json()
        else:
            print(f"Failed to retrieve flight data. Status code: {response.status_code}")
            return None

    def data_to_df(self, response):
        
        col_names = ['icao24', 'callsign', 'origin_country', 'time_position', 'last_contact', 'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source', 'category']

        df = pd.DataFrame(response['states'])
        df.columns = col_names

        # creating cols api_call_timestamp, bbox_country
        df['api_call_timestamp'] = datetime.datetime.fromtimestamp(int(response['time'])).strftime('%Y-%m-%d_%H:%M')
        df['bbox_country'] = self.country

        return df

    def df_transformations(self, df):

        aircraft_category_dict = {
            0: 'No information at all',
            1: 'No ADS-B Emitter Category Information',
            2: 'Light (< 15500 lbs)',
            3: 'Small (15500 to 75000 lbs)',
            4: 'Large (75000 to 300000 lbs)',
            5: 'High Vortex Large (aircraft such as B-757)',
            6: 'Heavy (> 300000 lbs)',
            7: 'High Performance (> 5g acceleration and 400 kts)',
            8: 'Rotorcraft',
            9: 'Glider / sailplane',
            10: 'Lighter-than-air',
            11: 'Parachutist / Skydiver',
            12: 'Ultralight / hang-glider / paraglider',
            13: 'Reserved',
            14: 'Unmanned Air Vehicle',
            15: 'Space / Trans-atmospheric vehicle',
            16: 'Surface Vehicle - Emergency Vehicle',
            17: 'Surface Vehicle - Service Vehicle',
            18: 'Point Obstacle(includes tethered balloons)',
            19: 'Cluster Obstacle',
            20: 'Line Obstacle'
        }

        position_src_dict = {
            0: 'ADS-B',
            1: 'ASTERIX',
            2: 'MLAT',
            3: 'FLARM'
        }

        # convert unix timestamps to datetime
        df['time_position'] = [datetime.date.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M') for ts in df['time_position']]
        df['last_contact'] = [datetime.date.fromtimestamp(int(ts)).strftime('%Y-%m-%d %H:%M') for ts in df['last_contact']]

        # map default values to dict values
        df['category'] = [aircraft_category_dict[category] for category in df['category']]
        df['position_source'] = [position_src_dict[src] for src in df['position_source']]

        return df
    
    def df_final(self, df):
        final_cols = ['api_call_timestamp', 'bbox_country', 'origin_country', 'icao24', 'callsign', 'time_position', 'last_contact', 'longitude', 'latitude', 'baro_altitude', 'on_ground', 'velocity', 'true_track', 'vertical_rate', 'sensors', 'geo_altitude', 'squawk', 'spi', 'position_source', 'category']

        df = df.filter(items=final_cols)
        df.reset_index(drop=True, inplace=True)

        return df
    
    def get_flights_df(self):
        flights_json = self.get_flight_data()
        df = self.data_to_df(flights_json)
        df = self.df_transformations(df)
        df = self.df_final(df)
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

        return df





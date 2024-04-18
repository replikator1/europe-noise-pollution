import pandas as pd 
import time
import random
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(file_names_filtered: list, *args, **kwargs):
    # Initial conditions
    day = datetime.today().day - 1 
    date = f'2024-04-{day:02}'
    sensor_type = 'laerm'
    url = f'https://archive.sensor.community/{date}/'

    # Define schema
    pollution_schema = {
        'sensor_id':pd.Int64Dtype(), 
        'sensor_type':str,
        'location':pd.Int64Dtype(),
        'lat':float,
        'lon':float,
        'noise_LAeq':float,
        'noise_LA_min': float,
        'noise_LA01': float,
        'noise_LA95':float,
    }
    parse_dates = ['timestamp']
    # Download files
    df = pd.DataFrame()
    i, z = 1, len(file_names_filtered)

    for file_name in file_names_filtered: 
        df_temp = pd.read_csv(url+file_name, sep=';', dtype=pollution_schema, parse_dates=parse_dates)
        df = pd.concat([df, df_temp])
        print(f'{i}/{z} done!')
        #time.sleep(random.uniform(0.2,1))
        i += 1
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

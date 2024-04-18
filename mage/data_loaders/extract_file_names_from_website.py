import requests
from bs4 import BeautifulSoup
import os
import time
import random
import pandas as pd
from datetime import datetime

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    # Initial conditions
    day = datetime.today().day - 1
    date = f'2024-04-{day:02}'
    sensor_type = 'laerm'
    url = f'https://archive.sensor.community/{date}/'
    
    # Fetch HTML content
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Parse content and extract file names
    a_tags = soup.find_all('a')
    file_names = [a_tag.get_text() for a_tag in a_tags if a_tag.get_text()[-3:] == 'csv']
    
    # Filter names to get only required sensors
    file_names_filtered = [fn for fn in file_names if sensor_type in fn]
    
    #return file_names_filtered
    return file_names_filtered

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

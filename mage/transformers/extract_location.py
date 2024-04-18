import reverse_geocode
import pandas as pd 
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Extract location based on latitude and longitude
    df_location = data[['lat' , 'lon']]
    # Drop duplicates
    df_location_distinct = df_location.drop_duplicates()
    # Creating a zip with location, latitudes and longitudes
    lats=df_location_distinct['lat'].to_list()
    lons=df_location_distinct['lon'].to_list()
    coords = list(zip(lats, lons))
    find_info = reverse_geocode.search(coords)
    df_location_info = pd.DataFrame(columns=['lat', 'lon', 'country_code', 'city_name', 'country'])
    for f in zip(coords, find_info):
        row = list(f[0]) + list(f[1].values())
        df_location_info.loc[len(df_location_info)] = row

    return df_location_info

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

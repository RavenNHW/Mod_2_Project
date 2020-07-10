def return_clean_dataframe():
    #load pandas, numpy
    import pandas as pd
    import numpy as np

    # Import the Data
    df = pd.read_csv('./data/kc_house_data.csv')

    # Convert Date to Datetime:
    df['date'] = pd.to_datetime(df['date'])

    # Create yr_sold column:
    df['yr_sold'] = df.date.dt.year

    # Create "was renovated" column (NOT TESTED)
    reno_mask_zeros = df['yr_renovated'] != 0
    reno_mask_nas = df['yr_renovated'].notna()
    reno_mask = reno_mask_zeros & reno_mask_nas
    df['was_renovated'] = reno_mask

    # Checking to make sure sqft_basement is zero at ? values -- In 170 cases it is not
    # int_basement = pd.to_numeric(df.sqft_basement, errors='coerce', downcast='integer')
    # int_basement.value_counts()
    # int_basement.fillna(0, inplace=True)
    # check_vals = df.sqft_living - int_basement
    # df.loc[df.sqft_above != check_vals, ['sqft_living', 'sqft_above', 'sqft_basement']]

    # Impute sqft_basement from sqft_living - sqft_above
    df['sqft_basement'] = df.sqft_living - df.sqft_above
    
    # Adjusting an assumed typo of a house having 33 bedrooms
    df.iat[15856, 3] = 3
    
    # Adjusting the 11 bedroom house's bedroom and bathroom counts after finding the correct values
    # https://www.zillow.com/homedetails/5049-Delridge-Way-SW-Seattle-WA-98106/48755748_zpid/
    df.iat[8748, 3] = 4
    df.iat[8748, 4] = 1

    # Replace yr_renovated with yr_built where = either 0 or NaN
    df['yr_renovated'] = df['yr_renovated'].fillna(df['yr_built'])
    df['yr_renovated'] = df['yr_renovated'].replace(0, df['yr_built'])
    
    # Adjusting 18 entries that have a renovated year of 2015 to align with the year they were 
    # sold (2014), so that our Effective Age column will have no negative entries
    for i in df.loc[(df.yr_renovated > df.yr_sold)].yr_renovated.index:
        df.iat[i, 15] = df.iat[i, 21]

    # Create Effective Age Column
    df['effective_age'] = df['yr_sold'] - df['yr_renovated']

    # Create Log-Scaled Price Column
    df['log_price'] = np.log(df.price)
    
    # Chose to cut houses greater than 8,000 sq feet, as we felt those weren't representative of our target audience.
    df = df[df.sqft_living < 8000]

    # Create a function for computing (as the crow flies) Distance between
    # Space needle and given lat/long
    def distance_from_space_needle(lat, long):
        """return 'as the crow flies' distance in miles from the 
        space needle, given latitude and longitude coordinates of a location"""
        # Convert lat/longitudes to radians
        def to_radians(latlong):
            return latlong / 57.29577951
        # lat/long of space needle
        space_lat = to_radians(47.6205)
        space_long = to_radians(-122.3493)
        # lat/long of input
        loc_lat = to_radians(lat)
        loc_long = to_radians(long)
        # distance in miles
        d = 3963.0 * np.arccos((np.sin(space_lat) * np.sin(loc_lat))\
                               + np.cos(space_lat) * np.cos(loc_lat)\
                               * np.cos(loc_long - space_long))
        return d

    # Create Distance from Space Needle Column:
    df['space_needle_dist'] = distance_from_space_needle(df.lat, df.long)

    # Create a Function for computing the bearing relative from space needle
    # of a given lat/long point
    def needle_bearing(lat, long):
        """return bearing theta in radians for given location's
        bearing relative to the space needle. Takes latitude and longitude
        of the location."""
        space_lat = 47.6205
        space_long = -122.3493
        delta_fi = np.log(np.tan(space_lat / 2 + np.pi/4) / np.tan(lat / 2 + np.pi/4))
        delta_lon = abs(space_long - long)
        bearing = np.arctan2(delta_lon, delta_fi)
        return bearing

    # Create Space Needle Bearing Column
    df['space_needle_bearing'] = needle_bearing(df.lat, df.long)

    # Create set of duplicated IDs
    duplicated_ids = df[df.id.duplicated()].id
    
    # Return df, duplicated_ids
    return df.to_pickle('./data/cleaned_df.pkl')
return_clean_dataframe()

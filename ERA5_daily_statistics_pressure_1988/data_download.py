import cdsapi

# define dataset and request
dataset = "derived-era5-pressure-levels-daily-statistics"
request = {
    "product_type": "reanalysis",
    "variable": ["specific_cloud_liquid_water_content"],
    "year": "1988",
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "data_format": "netcdf",
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "pressure_level": ["1"],
    "daily_statistic": "daily_mean",
    "time_zone": "utc+00:00",
    "frequency": "6_hourly",
    "area": [50, -126, 24, -65],
}

# output file name
filename = "rough_CONUS_pressure_clwc_1988.nc" 

# initialize client, fetch dataset
client = cdsapi.Client()
result = client.retrieve(dataset, request)

# download and save as custom name
client.download(result, [filename])

import cdsapi

dataset = "derived-era5-single-levels-daily-statistics"
request = {
    "product_type": "reanalysis",
    "variable": ["total_precipitation"],
    "year": "1988",
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
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
    "daily_statistic": "daily_mean",
    "time_zone": "utc+00:00",
    "frequency": "6_hourly",
    "area": [50, -126, 24, -65]
}

# output file name
filename = "rough_CONUS_daily_single_precipitation_1988.nc" 

# initialize client, fetch dataset
client = cdsapi.Client()
result = client.retrieve(dataset, request)

# download and save as custom name
client.download(result, [filename])

import cdsapi

# define dataset and request
dataset = "derived-era5-pressure-levels-daily-statistics"
dataset = "reanalysis-era5-pressure-levels-monthly-means"
request = {
    "product_type": ["monthly_averaged_reanalysis"],
    "variable": ["temperature"],
    "pressure_level": ["1000"],
    "year": ["1988"],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "time": ["00:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [50, -126, 24, -65]
}

# output file name
filename = "rough_CONUS_temperature_1988.nc" 

# initialize client, fetch dataset
client = cdsapi.Client()
result = client.retrieve(dataset, request)

# download and save as custom name
client.download(result, [filename])

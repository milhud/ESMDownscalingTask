# ESMDownscalingTask1

This repository contains my work regarding the first exercise for the ESM Downscaling project. The subdirectories listed above contain code to download, process, and analyze [ECMWF Reanalysis v5 (ERA5) data](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5).

The following datasets were analyzed:

- [ERA5 monthly averaged data on pressure levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=overview)
- [ERA5 monthly averaged data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-single-levels-monthly-means?tab=overview)
- [ERA5 post-processed daily statistics on pressure levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/derived-era5-pressure-levels-daily-statistics?tab=overview)
- [ERA5 post-processed daily statistics on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/derived-era5-single-levels-daily-statistics?tab=overview)
- [ERA5 hourly data on pressure levels from 1940 to present](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=overview)
- [ERA5 hourly data on single levels from 1940 to present](https://cds.climate.copernicus.eu/datasets?q=era5&kw=Variable+domain%3A+Atmosphere+%28surface%29&kw=Variable+domain%3A+Atmosphere+%28upper+air%29&kw=Variable+domain%3A+Atmosphere+%28upper+level%29&kw=Variable+domain%3A+Ocean+%28physics%29)

Each dataset has been analyzed in the following way:

1. Downloaded
   - The data was downloaded using the CDSAPI with the associated naming convention, and placed into the data subdirectory.
   - For data for single levels, "2m temperature" and "Total Precipitation" were the variables analyzed
   - For data on pressure levels, "Specific cloud liquid water content" (CLWC) and "Temperature" were variables analyzed on the first pressure level (1 hPa)
2. Preprocessed
   - Due to rate limits and size requirements, it was necessary in some instances to download the data separate and then merge it using xarray's built in merge function
   - The dataset was then clipped to fit the continental United States using GeoPandas ([shapefile downloaded from the Census](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html)).
3. Annual Average
    - A heatmap was generated and saved, representing the variation of each variable across the United States
    - Similarly, a time series representing the variation of both variables throughout the year was created and saved.
4. Seasonal Statistics
    - Seasonal statistics were calculated with respect to temperature.
    - Each dataset had different representations, including but not limited to: box plots, tables, stem plots, and pie charts
5. Variation, Correlation
    - Finally, graphs were generated showing the correlation between the two variables.
    - The graphs include, but are not limited to: heatmaps, scatter plots, and violin plots

(Note: not all datasets are available in this repository; due to size requirements, some were omitted.)

Additionally, eferences to external sources/documentation have been documented when referenced.

---

You can access the direct links to the plots here:

- [ERA5 post-processed daily statistics on pressure levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_daily_average_pressure_1988/plots)
- [ERA5 post-processed daily statistics on single levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_daily_average_single_1988/plots)
- [ERA5 monthly averaged data on pressure levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_monthly_average_pressure_1988/plots)
- [ERA5 monthly averaged data on single levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_monthly_average_single_1988/plots)
- [ERA5 hourly data on pressure levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_hourly_average_pressure_1988/plots)
- [ERA5 hourly data on single levels from 1940 to present](https://github.com/milhud/ESMDownscalingTask/tree/main/ERA5_hourly_average_single_1988/plots9)


### Download This Directory

To download this directory, start by cloning it:

```bash
git  clone https://github.com/milhud/ESMDownscalingTask.git
cd ESMDownscalingTask
```

Then, make sure you have all of the requirements installed.

```bash
pip install -r requirements.txt
```

Additionally, make sure you register for an API key; place this in the home directory. Note: the analysis was run with Python 3.11.9






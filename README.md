# Temperature Converter

A NumPy-based project that generates, analyzes, and visualizes daily temperature data for a full year.

## What It Does

- Generates realistic daily temperatures for 364 days (52 weeks)
- Converts temperatures from Celsius to Fahrenheit
- Finds the hottest and coldest days of the year
- Calculates average temperature for each week
- Identifies the hottest and coldest weeks
- Saves data to CSV file for analysis

## Features

✅ Realistic temperature range (-10°C to 45°C)
✅ Automatic unit conversion (C to F)
✅ Weekly aggregation and analysis
✅ Hottest/coldest day and week identification
✅ Data export to CSV

## Data

- **Days**: 364 (52 weeks × 7 days)
- **Temperature Range**: -10°C to 45°C
- **Output Unit**: Fahrenheit

## Usage

```bash
python temperature_converter.py
```

Output will show:
- All daily temperatures in Fahrenheit
- Hottest day and temperature
- Coldest day and temperature
- Weekly average temperatures
- Hottest week and coldest week

## Output Files

- `temperature_data.csv` — Raw temperature data for all 364 days

## What You Learn

- NumPy array creation and reshaping
- Broadcasting for unit conversion
- Finding min/max values with `np.argmin()` and `np.argmax()`
- Array aggregation with `np.mean()` and `axis` parameter
- Saving data to CSV files

## Next Steps

This data can be visualized with Matplotlib or analyzed further with Pandas for trend analysis and forecasting.

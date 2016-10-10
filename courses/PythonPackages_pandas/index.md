---
---

# The Pandas Library

Andrew Tedstone, October 2016 

[Pandas website](pandas.pydata.org)

Pandas is your data analysis toolkit. It's the best option for opening up all sorts of datasets, checking them, quickly plotting them, manipulating them, computing statistics using Pandas-aware packages, and exporting to new files. 

Below is a very brief tutorial that covers the most important aspects of the package. For more info, check out the tutorials and documentation on the website above. I also recommend the book 'Python for Data Analysis' by Wes McKinney, who wrote the Pandas software.


## Toy weather data

The file weather.csv contains a few days of selected weather data from Solheimajokull, a glacier in southern Iceland.

We're going to use it as an example dataset for Pandas. In this case, the data are labelled with dates and times, but you don't have to use Pandas like this - you can load up any tabulated data you like.


## Open the data

Let's use the Pandas function that loads CSV files into a Pandas DataFrame:

```python
import pandas as pd
weather = pd.read_csv('weather.csv', index_col='Date', parse_dates='True')
```

Take a quick look at what the dataset contains:

```python
weather.head()
```
```
Out[23]: 
                     AirTemp  Humidity  WindSpd
Date                                           
2013-08-28 17:00:00     12.1      63.8      0.3
2013-08-28 17:30:00     10.8      72.6      1.4
2013-08-28 18:00:00     10.5      73.5      2.0
2013-08-28 18:30:00      9.7      74.5      1.2
2013-08-28 19:00:00      9.8      75.9      1.8

```

The `head()` command shows us the structure of the dataset and the first few lines of data. Here we can see that we have three columns: Air Temperature, Humidity and Wind Speed. These are all indexed, or labelled, together by Date.

Let's look at the air temperatures first:

```python
weather['AirTemp'].plot()
```

Pandas pops up a plot labelled with the dates and the name of the time series you are looking at.

Now close the window.

You can pull out bits of data by date or time. Let's just look at the data for 29 August 2013:

```python
print(weather['2013-08-29'])
```

Or you can pull out a range of dates and times, in this case just for 6 hours of the 29th Aug:

```python
print(weather['2013-08-29 15:00':'2013-08-29 21:00'])
```

At the moment, we can see that the data have a 30 minute resolution. What about daily averages?

```python
weather_daily_avg = weather.resample('24H').mean()
weather_daily_avg['WindSpd'].plot()
```

Using our original 30-minute data, we can also look at average temperature throughout a 24 hour cycle. To do this we need to 'group' the data by hour of the day and then take the average of all those values.

```python
temp_cycle = weather['AirTemp'].groupby(weather.index.hour).mean()
temp_cycle.plot()
```

If you want, you can compare this average daily temperature cycle back to the full temperature time series. Hopefully you'll see that the peak temperature of around 9.5 degrees C at 18:00 is a feature of the original data set.

Lastly, let's export our average daily values to a new file:

```python
weather_daily_avg.to_csv('weather_daily_avg.csv')
```
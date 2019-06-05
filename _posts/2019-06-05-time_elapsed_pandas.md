---
layout: post
title: Calculating time elapsed using timestamp information in pandas
categories: Python
---

Given a set of dates and times, we want to calculate the time elapsed of each row relative to the first entry. A csv file containing dates and times is available for you to download [here]({{ site.baseurl }}/attachments/time_data.csv).

To start with we'll import the library and read in the data. The data has no header row, so we'll add one.

```python
import pandas as pd

names=['date', 'time']
df=pd.read_csv("time_data.csv", names=names)
df.head()
# >          date      time
# > 0  05/06/2019  14:01:10
# > 1  05/06/2019  14:09:30
# > 2  05/06/2019  14:17:50
# > 3  05/06/2019  14:26:10
# > 4  05/06/2019  14:34:30
```

Now we want to create a new column that combines the date and time stamp - the last option is key as (in our case) want the day reported before the month and not the other way around. Adjust this according to how you've structured your data

```python
df['datetime']=pd.to_datetime(df['date'] + ' ' + df['time'], dayfirst=True) 
df.datetime.head()
# > 0   2019-06-05 14:01:10
# > 1   2019-06-05 14:09:30
# > 2   2019-06-05 14:17:50
# > 3   2019-06-05 14:26:10
# > 4   2019-06-05 14:34:30
# > Name: datetime, dtype: datetime64[ns]
```
We can now check what the types of our different columns are.

```python
# check the datatypes of the dataframe
df.dtypes
# > date                object
# > time                object
# > datetime    datetime64[ns]
# > dtype: object
```

Before we create a column of the elapsed time, let's do a quick check to see if our results make sense. 

```python
startTime = df.datetime.loc[0] # Timestamp('2019-06-05 14:01:10')
endTime = df.datetime.loc[1] # Timestamp('2019-06-05 14:09:30')
print(endTime-startTime)
# > Timedelta('0 days 00:08:20')
```

Given a start time of `2019-06-05 14:01:10` and an end time of `2019-06-05 14:09:30`, the reported difference of `0 days 00:08:20` makes sense. If you have timestamps on consequtive days but are getting differences reporting say `30 days 00:08:20`, then it's likely that your timestamp is formatted with the days and months the otherway around - in this case format it accordingly as when we made the `datetime` column with `pd.datetime` and the `dayfirst` option. This is a common error if switich between say UK and US datetime formats.

Now we know the elapsed time is working, we can scale this up to the whole dataframe.

```python
## NB/
## position << this is a list of the locations of the datetime column within the larger dataframe
## df.iloc[0, position] << this is the first (0) position in the list of positions
## df.iloc[1:, position] << this is the second (1) to the last position in the list of positions
position = df.columns.get_loc('datetime')
df['elapsed'] =  df.iloc[1:, position] - df.iat[0, position]

# Check it
print(df.head())

# >          date      time            datetime  elapsed
# > 0  05/06/2019  14:01:10 2019-06-05 14:01:10      NaT
# > 1  05/06/2019  14:09:30 2019-06-05 14:09:30 00:08:20
# > 2  05/06/2019  14:17:50 2019-06-05 14:17:50 00:16:40
# > 3  05/06/2019  14:26:10 2019-06-05 14:26:10 00:25:00
# > 4  05/06/2019  14:34:30 2019-06-05 14:34:30 00:33:20

print(df.tail())

# >            date      time            datetime         elapsed
# > 295  07/06/2019  06:59:30 2019-06-07 06:59:30 1 days 16:58:20
# > 296  07/06/2019  07:07:50 2019-06-07 07:07:50 1 days 17:06:40
# > 297  07/06/2019  07:16:10 2019-06-07 07:16:10 1 days 17:15:00
# > 298  07/06/2019  07:24:30 2019-06-07 07:24:30 1 days 17:23:20
# > 299  07/06/2019  07:32:50 2019-06-07 07:32:50 1 days 17:31:40
```

Now, `df.elapsed` is of a timedelta type which has various methods. You can get things out of it like seconds, hours days etc. For example, we can get the seconds out of it like this:

```python
seconds=df.elapsed.dt.total_seconds() 
seconds.head()

# > 0       NaN
# > 1     500.0
# > 2    1000.0
# > 3    1500.0
# > 4    2000.0
```
Careful if you just use `df.elapsed.dt.seconds` as that'll revert to zero if your day changes.






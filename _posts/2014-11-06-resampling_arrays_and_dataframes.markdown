---
layout: post
title: Resampling arrays and dataframes 
categories: Python R
tags: python, R, resample, skip rows, array, dataframe
---

I've been experimenting with various different tools recently and for speed required 
smaller but representative data from my current project. Here are two ways of getting 
every nth line of an array (python) or dataframe (R):

Python: 

```python
# assume n = 10
resampled_array = array[0::10]
```

R: 

```r
# assume n = 10
Nth.row <- function(dataframe, n) dataframe[(seq (n, to=nrow(dataframe), by=n)),]
resampled_df <- Nth.row(df, 10)
```

Tags: python, R, resample, skip rows, array, dataframe

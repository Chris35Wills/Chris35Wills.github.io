---
layout: post
title: Thinning your data out with pandas
categories: Python, data
---

When compiling large datasets, you may end up with values in some columns that make up only a small contribution of the total. ***These values may be important and should not just be discarded without careful consideration.*** Equally, if they van be discarded, the below helper function can assist - given a dataframe, a specified column (of categorical data) and a threshold cutoff, any values within the column that make up less than the threshold contribution to the total will result in that row of the dataframe being dropped.

This is especially useful when using the input dataframe for plotting for further analysis.

```python
def thin_data(data, variable_to_consider, percentage_cutoff=10, verbose=True):
	"""
	Takes in a dataframe and removes rows where the contribution of categorical variables in a specified column make up 
	less than a defined percentage of the total 

	data=pandas dataframe
	variable_to_consider=name of column
	percentage_cutoff=where entries in the variable_to_consider column make up less than this percentage, they will be dropped

	RETURNS dataframe 
	"""

	if verbose:
		print("*****")
		print("Trimming dataframe")
		print("Column: %s " %variable_to_consider)
		print("Dropping rows where %s variables make up less than %i %% of the total column composition." %(variable_to_consider,percentage_cutoff))
		print(" ")
		print("%s : %% of total" %variable_to_consider)
		print("----------------")
		print((data[variable_to_consider].value_counts()/data[variable_to_consider].count())*100)
	
	class_percents=(data[variable_to_consider].value_counts()/data[variable_to_consider].count())*100
	class_percents_lessThan_CUTOFF=class_percents[class_percents<percentage_cutoff]
	class_percents_greaterThan_CUTOFF=class_percents.drop(class_percents_lessThan_CUTOFF.index)

	# drop rows where CLASS is > specified percentage 
	#help: https://stackoverflow.com/questions/12065885/filter-dataframe-rows-if-value-in-column-is-in-a-set-list-of-values
	
	mask_gtCUTOFF=data[variable_to_consider].isin(list(class_percents_greaterThan_CUTOFF.index))
	data_trimmed=data[mask_gtCUTOFF]

	return(data_trimmed)
```

For a full example, check out this [jupyter notebook](https://github.com/Chris35Wills/data_notebooks/blob/master/thinning_pandas_df_on_percent.ipynb) on Github - feel free to adapt it as required.

 

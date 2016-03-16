---
---

# Reading tabulated data with numpy

Numpy excels when applied to matrix type calculations (see the [next section](../numpy_io_scipy_image)) however, it can be used to read in tabulated datasets - remember though that a numpy array must be all of the same type (e.g. float) so this won't work if your data is a mix of int, float and string data types.

Right click [this link](../radar_data.csv) and save the file to a location on your machine. 

To read in text data in numpy, we need to use the ```numpy.load_txt``` function:

```python
data=numpy.loadtxt('path/to/file/radar_data.csv', skiprows=1, delimiter=',', dtype='f')
```

It is important that you specify the delimiter (as the file is a .csv, we know this to be  a ','). You will also notice that we have used the ```skiprows``` option inherent of ```numpy.loadtxt```, enabling us to miss out the header matter included in the ```radar_data.csv```. This is important as the header matter is in string format which differs to the data in the columns, the format of which we have set to float type using the ```dtype``` option (have a look [here](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html) for more information on data types in numpy). Remember that all of the documentation, including details on additional option flags, can be found by typing ```help(nump.loadtxt)```. 

Note that ```numpy.loadtxt()``` doesn't work very well with keeping header info - hence us skipping that first line. For now, just remember:
		

		| Column  | Data                            |
		| :-----: |:-------------------------------:|
		|  1 	  | UTC_Seconds_Of_Day	            |
		|  2 	  | Lat(deg)	                    |
		|  3 	  | Long(deg)	                    |
		|  4 	  | WGS84_Ellipsoid_Height(m)	    |
		|  5 	  | S-to-N_Slp	                    |
		|  6 	  | W-to-E_Slp	                    |
		|  7 	  | RMS_Fit(cm)	                    |
		|  8 	  | Num_ATM_obs_Used	            |
		|  9 	  | Num_Of_ATM_obs_Removed          |	 
		|  10 	  | Dist_Block_To_Right_aircraft(m)	|
		|  11 	  | Track_ID					    |


We will touch on accessing using column names later on (although this kind of approach is better handled using a package like [pandas](http://pandas.pydata.org/)).

## Getting details about the array

By assigning the function call to ```data```, we have now created a new array object. We can now use the methods inherent of array to get some info about the data we have just read in:

	>>> data.shape
	>>> (6080L, 11L)

You can also find out details about specific columns within the data array object - for example, the maximum value in the second column can be found using:

	>>> data[:,1].max()
	>>> 82.329346000000001

and the mean value of the 4th column can be found using:

	>>> data[:,3].mean()
	>>> 15.891525690789475

## Accessing specific parts of your data

The data stored in the array can be indexed and sliced using the methods covered [here](../numpy_indexing). This allows you to pull out specific data from the data object - keep in mind the dimensions as calculated above. 

To get the first column:

```python
time=data[:,0]
```

to access the 2nd, 3rd and 4th columns:

```python
xyz=data[:,1:4]
```

and to access the first 10 rows:

```python
subsample=data[0:10,:]
```

In each of the examples above, we assigned the slice to a new variable resulting in the development of a set of new arrays. Again, you can use the functions of array to pull out some information. To calculate the maximum value in the time object:

	>>> time.max()
	>>> 44310.25

## Manipulate the values

What we can also do is alter the values held within the array. For example, say we want to reduce the values in the ```time``` array (which have units of UTM seconds according to the header matter of ```radar_data.csv```) by 100 - all we have to do is:

```python
time_offset=time[:]-100
```

Notice that we assign this to a new array to ensure that the changes are stored - for this simple 1-dimensional case (have a look at ```time.shape```), we could also have typed:

```python
time_offset=time-100
```

### Indexing and subsampling using conditions

A handy trick to be aware of is the ability to pull out/manipulate data meeting specific conditions. Using the ```time``` array, we can find the mean:

```python
mean=time.mean()
```

If we only want to get values from the ```time``` array greater than the mean time value, we can use:

```python
time_gt_avg=time[time > mean]
```

If we want to reduce all values equal to mean to zero (which may not be advisable, but for purposes of providing an example!):

```python
time[time > mean] = 0
```

Notice that this last command changes the values within the actual ```time``` array.

[Where there are more dimensions, more complicated indexing has to be employed to make changes to specific columns of data. The ```xyz``` array made above contains the data detailing latitude, longitude and elevation of a series of points. Let's say that we know that the elevation values (the 3rd column in xyz, accessed using ```xyz[:,2]```) are overestimated by 10 metres and that we want to correct them. This correction can be carried out using:]:#

[```python]:#
[xyz[:,2] = xyz[:,2]-10]:#
[```]:#

[Another way to do this (more code but maybe you find it easier to read) would have been to first slice the data to 2 arrays:]:#

[```python]:#
[xy=data[:,1:3]]:#
[z=data[:,3]]:#
[```]:#

[then correct the z values:]:#

[```python]:#
[z=z[:]-10]:#
[```]:#

[Now stick everything together:]:#

[```python]:#
[numpy.column_stack((xy,z))]:#
[```]:#

## Write out data to a new file

To write out an array to a new file, you can use ```numpy.savetxt()```. Let's save the xyz subset to a file called ```xyz_subsample.csv```:

```python
numpy.savetxt("/path/to/save/to/xyz_subsample.csv", xyz, delimiter=",")
```

# Other things to know and consider

## Alternative packages for data wrangling

If you are going to be spending a lot of time working with tabulated datasets, I would advise you to spend some time familiarising yourself with [pandas](http://pandas.pydata.org/). Pandas offers an extremely efficient (and arguably more readable) approach to dealing with these kinds of data sets - a handy reference for the efficient use of pandas can be found [here](http://shop.oreilly.com/product/0636920023784.do).

## Accessing data using column names in numpy (if you don't want to use pandas)

If you know the column names, it is possible to integrate these by creating a [structured array](http://docs.scipy.org/doc/numpy/user/basics.rec.html#module-numpy.doc.structured_arrays) - have a look at the documentation.

For example, let's create an array:

```python
new_data = np.array([(4,3,3,'some'),(5,4,3,'other'),(6,3,2,'useful'),(3,9,7,'info'),(8,4,6,'to'),(8,3,3,'use')])
```

This will result in everything being made a string data format:

	>>> new_data.dtype
	>>> dtype('S11')

What we need to do is to assign the format of each column type - at the same time, we can give that column a label attribute:

```python
new_data = np.array([(4,3,3,'some'),(5,4,3,'other'),(6,3,2,'useful'),(3,9,7,'info'),(8,4,6,'to'),(8,3,3,'use')],dtype=[('x','f'),('y','f'),('z','f'),('text','S11') ])
```

Note that the dtype ```S11``` represents an 11 character string (see here for more [data type information](http://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)).

What you can now do is access elements of ```new_data``` by column name as defined when assigning the data type of each column such as:

```python
new_data['text']
new_data['x']
```

# [Previous](../numpy_indexing) [Home](../README_numpy) [Next](../numpy_io_scipy_image)




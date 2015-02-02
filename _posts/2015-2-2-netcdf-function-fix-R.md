---
layout: post
title: Fixing errors associated with R's ncdf "get" function
categories: R, File I/O
tags: R, NetCDF
---

Reading in data from netcdf files can be a bit of a pain the first few times you have to deal with them - this is rarely helped by error occurrences that mean next to nothing to you. Whilst trying to get some variable data ("z") from a netcdf file associated with a newly defined R object "my_z" as here:

{% highlight R %}    
> ex.nc = open.ncdf(dir.nc) # open netcdf file
> my_z = getx.var.ncdf( ex.nc, "z", verbose=TRUE) # assign data to variable   
{% endhighlight %} 

I was receiving the error:

```
"Error in mv * 1e-05 : non-numeric argument to binary operator"
```

The fix for this was found [here](http://thr3ads.net/r-help/2010/10/1040427-non-numeric-argument-to-binary-operator-error-while-reading-ncdf-file) followed by [here](http://climateaudit.org/2009/10/10/unthreaded-23/) and requires a re-definition of the ncdf package function "get.var.ncdf". As per the original post I found fixing this, follow this protocol so get rid of the error:

[1] Print out the function get.var.ncdf by typing exactly that in the console
[2] Copy the results to a new script window
[3] Redefine the function as getx.var.ncdf
[4] Find the two places in the function where it says: " mv <- nc$var[[nc$varid2Rindex[varid]]]$missval "
[5] Replace each with: mv = -1.000000e+30
[6] Run the new function: "data1 <- getx.var.ncdf( nc, v1 )" will retrieve the data.

If you want to just copy and paste the "fixed function - now called getx.var.ncdf - you can get a copy [here](https://gist.github.com/27b3ed192b7b38c564d4.git).


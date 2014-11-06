---
layout: post
title: Calculating the convex hull of a point data set (Python)
categories: Python
tags: python scipy convex hull lidar
---

Working with LiDAR point data it was necessary for me to polygonize the point cloud extent. A first approach was to calculate the convex hull of the points.
This is predominantly facilitated using scipy spatial's [ConvexHull](http://docs.scipy.org/doc/scipy-dev/reference/generated/scipy.spatial.ConvexHull.html) function.

Using a resampled xy point file I managed to get the following:

####IMAGE OF ORIGINAL INPUT POINTS#
####IMAGE OF HULL POINTS#

For my application I required the hull points to be printed out into a txt/csv in order of position (i.e. going clockwise around the hull). This is enabled by simply 
pulling out the "vertices" from the spatial.ConvexHull object - this gives the indicies of the convex hull points within the original xy input file:


```
hull = spatial.ConvexHull(xy_file, qhull_options="Qt")
hull_indices = hull.vertices
```

This is all integrated into a single function:

```
import os
import sys
import numpy as np
from scipy import spatial

def xy_convex_hull(input_xy_file):
	'''
	Calculates the convex hull of a given xy data set
	returning the indicies of the convex hull points
	in the input data set. A convex hull point
	co-ordinate file is then created using
	write_convex_hull_xy()
	'''
	if os.path.isfile(input_xy_file):
		print "Loading file...."
		xy_file = np.loadtxt(input_xy_file, usecols= (0,1))
	else:
		sys.exit("File for convex hull calculation doesn't exist")
	
	print "Calculating hull points..."
	hull = spatial.ConvexHull(xy_file, qhull_options="Qt")
	hull_indices = hull.vertices

	print "Found %d hull points" % len(hull_indices)
	print "Hull indicies calculated and now being returned..."

	return xy_file, hull_indices

```

hull_indicies - which more precisely are the "[i]ndices of points forming the simplical facets of the convex hull" - will look something like this:

```
array([17218337,    48757,     3476,     1517,      649,       73,

             38,       37,        1,        0,      209,    27606,

         153490,   154907,  1422687,  1435840,  1455472,  1933477,

        2183734,  2185942,  2754182,  2977613,  3100991,  7573831,

        8619400, 14809551, 15214362, 16139836, 16146528, 16188976,

       16204639, 16351763, 16649880, 17150945, 17153685, 17260738,

       17268373, 17273051, 17275385, 17299918, 17300751, 17304440,

       17307723, 17318805, 17319327, 17319315, 17319198, 17290692,

       17286814, 17282596, 17279306], dtype=int32)
```

The hull vertex indices (hull_indices) can then be passed in with the main xy point file (xy_file) (along with an output path (opath) and output file name (file_name)
to the below function which writes out the xy positions of hull_indices from xy_file (in the format I required):

```
def write_convex_hull_xy(xy_file, hull_indices, opath, file_name):
	'''
	Takes the convex hull verticies (an array of indicies) and
	uses them to extract and write out the convex hull vertex
	co-ordinates to a file
	'''
	
	file_name = "%sconvex_hull_vertices_%s.txt" %(opath, file_name)
	f = open( file_name, 'w')
	
	for i in range(len(hull_indices)):
		index = hull_indices[i]
		value_y = xy_file[index, 0].astype('float32')
		value_x = xy_file[index, 1].astype('float32')
		f.write("%f %f\n" %(value_y, value_x))

	f.close()
```

This should give something similar to the following:

```
540460.812500 7362116.000000

540473.875000 7362116.000000

540473.937500 7362116.000000

540475.687500 7362133.000000

540475.875000 7362134.500000

540478.750000 7362163.000000

                    ... etc.
```




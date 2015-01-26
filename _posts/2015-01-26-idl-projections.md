---
layout: post
title: Co-ordinate systems - Projecting data in IDL
categories: IDL, MapProjections, CoordinateSystems
tags: IDL MapProjections CoordinateSystems
---

There are three key commands you need to know about in IDL for projecting data

1. map_proj_init
2. map_proj_forward
3. map_proj_inverse

# map_proj_init

This sets the projection parameters required i.e. all details associated with the map projection
The projections are represented by a series of codes that can be found here: http://www.exelisvis.com/docs/MAP_PROJ_INIT.html

Syntax: 

	Result = MAP_PROJ_INIT( Projection [, ELLIPSOID=value] [, /GCTP] [, LIMIT=vector] [, /RADIANS] [, /RELAXED] ) ... + numerous keywords

Example: 

	> map=map_proj_init(106, datum=8, /gctp, center_latitude=71.0, center_longitude=321.)

# map_proj_forward

Takes in LON/LAT (notice the order) values and converts them to the projection set using map_proj_init (associated with some variable - in this case "map")
Returns Cartesian coordinates RELATIVE to the projection details. Where as the LON/LAT (notice the order) are in degrees, the return values here will [unless otherwise specified] be in metres relative to the set center_latitude and center_longitude values.

Syntax: 

	Result = MAP_PROJ_FORWARD(Longitude [, Latitude] [, CONNECTIVITY=vector] [, /FILL] [, MAP_STRUCTURE=variable] [, POLYGONS=variable] [, POLYLINES=variable] [,  /RADIANS] )

Example: 

	> result=map_proj_forward(data(1),data(0),map_structure=map)

# map_proj_inverse

Taking in the projection info set using map_proj_init and x/y values (that are directly associated with the projection parameters that map_proj_init specifies), returns LON/LAT (notice the order) values.

Syntax: 

	Result = MAP_PROJ_INVERSE (X [, Y] [, MAP_STRUCTURE=value] [, /RADIANS] )

Example: 

	> inverse=map_proj_inverse(result(0),result(1),map_structure=map)


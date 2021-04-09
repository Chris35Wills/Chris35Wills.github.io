---
layout: post
title: GDAL python scripts through osgeo4w (python 3)
categories: Python
---

Gdal offers many useful tools which I use in a daily basis including things like [gdal_calc](https://gdal.org/programs/gdal_calc.html).

In a windows environment, after installing gdal through [OSGeo4W](https://www.osgeo.org/projects/osgeo4w/), opening the OSGeo4W Shell and typing `o-help` lists the tools available. 

Installing a recent release of osgeo4w, I found that I could no longer find or run gdal_calc. After [reading around](https://gis.stackexchange.com/questions/273870/osgeo4w-shell-with-python3), I found it again by running `py3_env` in the osgeo4w shell. This sets up the shell for python 3.

Searching for gdal_calc using `where gdal_calc` could then locate gdal_calc again and all was well :)

You can also use Python 3 through the shell now by typing `python3`.
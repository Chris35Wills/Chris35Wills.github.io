---
layout: post
title: Add multiple csv files to QGIS quickly...
---

I often find myself with csv files that I'd like to visualise quickly in QGIS. If these were shape files, it is quick  and easy to load multiple files at once. This isn't the case with csv files as you have to set the columns etc. on a file by file basis. A bit of python enables you to do this quickly. This detailed fully [here](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html) but the below info provides a snippet.

First, in your QGIS session, open up the python console.

Now type the following into the console (and then press enter or return):

```python
import os.path, glob
layers=[] # makes an empty list
```

Let's say we have all of our csv files which we want to add in "C:/temp/" and the x and y coordinates in each files are titled **x** and **y**. We can now loop through the files in the directory, and assign the x and y columns:

First, in the python console, we are going to start a loop through all files in the path we have declared - the \* means **loop all files in this folder** which uses [glob](https://docs.python.org/2/library/glob.html).

```python
for file in glob.glob('C:/temp/*'): # Change this base path
```

On the next line we need to tell QGIS about our file structure (more about this and for different file types [here](http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html)). We will set this such that our file is of csv type, the x field is called **x** and the y field is called **y** and also that our coordinate system is epsg:3413:

```python
  uri = "file:///" + file + "?type=csv&xField=x&yField=y&spatialIndex=no&subsetIndex=no&watchFile=no&crs=epsg:3413"
```
We can now open up these layer by creating a QgsVectorLayer object - we add attributes to tell it details about **x** and **y**:

```python
  vlayer = QgsVectorLayer(uri, os.path.basename(file), "delimitedtext")
  vlayer.addAttributeAlias(0,'x')
  vlayer.addAttributeAlias(1,'y')
  layers.append(vlayer)
```
On running this in the console, if you don't set the coordinate system (crs) as part of the *uri* variable definition, you will be prompted to set the coordinate system for each file.

Finally, we add them to QGIS: 

```python
QgsMapLayerRegistry.instance().addMapLayers(layers)
```

So the whole lot of code looks like this:

```python
import os.path, glob
layers=[]

for file in glob.glob('C:/temp/*'): # Change this base path
  uri = "file:///" + file + "?type=csv&xField=x&yField=y&spatialIndex=no&subsetIndex=no&watchFile=no"
  vlayer = QgsVectorLayer(uri, os.path.basename(file), "delimitedtext")
  vlayer.addAttributeAlias(0,'x')
  vlayer.addAttributeAlias(1,'y')
  layers.append(vlayer)

QgsMapLayerRegistry.instance().addMapLayers(layers)
```




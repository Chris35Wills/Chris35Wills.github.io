---
layout: post
title: Joining vector datasets with duplicate field names with arcpy's fieldmappings object
categories: python
---

I've been looking for how to spatially join vector data using an older version of ArcGIS (v10.3) where the data being joined may contain duplicate attribute names. ArcGIS's python library `arcpy` provides access to the [fieldmappings object](https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/fieldmappings.htm) which can be manipulated to handle this which can be a bit tricky to get to grips with. Duplicated named attributes can be a problem as they can overwrite one another. Also, sometimes you want to keep a clear track of where different attributes in a dataset come from.

To layout an example: you want to spatially join two vectors, both of which are in the same coordinate system (an essential start!). 

Vector 1 contains the follow attributes:

* OVERVIEW
* GEOLOGY

Vector 2 contains the follow attributes:

* ELEVATION
* VELOCITY
* GEOLOGY

If you join these, aiming to keep all of the fields, as you have 2 GEOLOGY attribute fields, one will overwrite the other. In this case, I want to add a prefix (e.g. "v2") to the field names (and maybe alter them to keep under the 10 character name limit) in the output vector file so that it will contain variables:

* OVERVIEW
* GEOLOGY
* v2ELEV
* v2VEL
* v2GEOL

This is where you need manipulate the fieldmapping object. First you need to tell it which fields you want join, then an alternative name for those fields. The following function does all of this for you, where you have to provide:

* the file you want to join too (`inVec`)
* the file you want to take attributes from (`joinVec`)
* a string to use a prefix to the joined attribute field name in the output vector layer (`joinVec__name`)
* a dictionary of the fields to join and their new names (remember the prefix argument) (`specified_fields_dict`)

The function is as follows:

```
def get_fieldmappings_for_join(inVec, joinVec, joinVec__name, specified_fields_dict, DEBUG=False):
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Add all attributes to table from the main point file and the file you want to extract from
	# The attribs from the layer to exract from will have an additional labelling prefix
	# Then drop any that you don't want to keep using the list of variables specified using the "specified_fields" argument
	# This should then provide the correct field mappings object, handling multiple files with same named variables......
	#
	# VARIABLES
	#
	# inpnt - path of point file being used to extract to
	# joinVec - full path to layer to extract from
	# joinVec__name - string that identifies the joinVec (used as a label)
	# specified_fields_dict - dictionary of attribute names to keep where keys will be the attribute names in 
	# 			the dataset and values will be used as the attribute names in the output (max 10 characters) 
	#			e.g. specified_fields_dict={"Depth":"water_depth"} # where Data_Depth is the existing attribute name and "tide_depth" is the output attribute name

	# Create a fieldmapping object
	fieldmappings = arcpy.FieldMappings()
	
	#Add attributes of your "master" layer
	## You want all attributes from this one so JUST add the table
	if DEBUG: print("Adding main layer attributes to fieldmapping object")
	fieldmappings.addTable(inVec)
	see_fields_in_fieldmapping(fieldmappings, print_it=False)

	##Layer to extract from
	## You want to add fields you want to join in addition to the "master" layers attribs
	## The next steps will also add a prefix in case the same named fields already exist
	extract_layer_fields=arcpy.ListFields(joinVec)
	list_fields_target=list()
	for f in extract_layer_fields:
		list_fields_target.append(f.name)

	#get rid of encoding 
	list_fields_target = [str(r) for r in list_fields_target]

	#keep only the attributes listed in "specified_fields_dict"
	keep_me=list()
	for f_name in list_fields_target:
		if(f_name in specified_fields_dict.keys()):		
			keep_me.append(f_name)

	if DEBUG: print("Adding extraction layer attributes to fieldmapping object")
	for field_join in keep_me:
		print(field_join)
		field_map = arcpy.FieldMap()
		field_map.addInputField(joinVec, field_join)
		field = field_map.outputField
		#field.name = joinVec__name + '_' + field.name
		field.name = specified_fields_dict[field_join] # name it using the value of the equivalent key passed with the specified_fields_dict
		field.aliasName = field.name
		field_map.outputField = field
		fieldmappings.addFieldMap(field_map)

	if DEBUG:
		print("Attributes in fieldmapping object")
		see_fields_in_fieldmapping(fieldmappings, print_it=False)
	return(fieldmappings)
```
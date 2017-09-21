---
layout: post
title: Promise under evaluation error (R)
categories: R
tags: R, error
---

If you declare a function that does some stuff like this: 

```R
path="/path/to/somewhere"

get_xy<-function(transectName_inst,path=path){

	trans=as.character(transectName_inst)
	
	f=Sys.glob(transectName_inst)
	data=read.csv(f)

	xy=c(data$X[1],data$Y[1])
	
	return(xy)
}
```

and then try and use the function with say `lapply` e.g.

```R
xy=lapply(transectNames, FUN=get_xy) 
```

you'll get a "promise under evaluation error". The problem is that our path variable path is set as default to a global variable and we are now running into variable scope issues. One way to fix this is to construct our function as such:

```R
get_xy<-function(transectName_inst, path = get('original_path', envir = globalenv())){
	...
	}
```

which tells `lapply` where to look for the variable `path`. Help and reasoning for this can be found [here](https://stackoverflow.com/questions/45314208/how-to-avoid-promise-already-under-evaluation-warning-for-setting-default-argume) and [here](https://stat.ethz.ch/pipermail/r-help/2008-November/180902.html).


---
layout: post
title: Running a parallel loop in R
categories: R
tags: R parallel
---

A code snippet detailing how to run a loop in parallel in R. The code below creates multiple files (each with a random number in the title) with the text "testing 1,2,3..." written inside. Note that parellelisation has its own overhead. This means that depending on the task being run in the loop, sometimes running in parallel will actually take longer than a normal loop. The code below is adapted from [this post](https://stackoverflow.com/questions/38318139/run-a-for-loop-in-parallel-in-r).

```R
library(foreach)
library(doParallel)

#setup parallel backend to use many processors
cores=detectCores()
cl <- makeCluster(cores[1]-1) #not to overload your computer 
registerDoParallel(cl)

foreach(i=1:100) %dopar% {

	randomNumber=abs(ceiling(rnorm(1)*100)*-1)
	outf=paste0("./parallel_test/test_", randomNumber, ".txt")
	write("testing 1,2,3...", file=outf)

}

#stop cluster
stopCluster(cl)


# ... to rerun a parallel loop, you must re-register the cluster using makeCluster()
```


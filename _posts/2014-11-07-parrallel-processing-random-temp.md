---
layout: post
title: Problems of parallel processing - shared file names
categories: general
tags: csh, parallel processing, random
---

Ensure any temp files that may be written to don't run the risk of being accessed by scripts 
being run in parallel - this can result in confusing results - especially if your 
program doesn't crash!

I found a handy fix in csh (easily replicated in any other language) was to get into the habit 
of doing the following at the beginning of a script and then for different temporary files as 
required:

{% highlight csh %}
	#! /bin/csh

	% Create random number for temp file to avoid messing up when running script in parallel
	set random_number = `awk 'BEGIN {srand(); print int(rand()*3000)}'`

	# Make use of your temp file (here just appending variables to it)
	echo $variable_1 $variable_2 >> temp_$random_number
	echo $variable_3 $variable_4 >> temp_$random_number

	# Do what you need with temp_$random_number and then get rid of it		

	rm -f temp_$random_number
{% endhighlight %}  

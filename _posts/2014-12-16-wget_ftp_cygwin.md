---
layout: post
title: Bulk data downloads using FTP
categories: Python, flight
tags: python flight
---

I've been needing to download vast amounts of data from various source recently including from the [NSIDC](http://nsidc.org/). As with the NSIDC, there are various ways made available to you to download data. One useful area is the http file directory that can be accessed such as [here](ftp://n5eil01u.ecs.nsidc.org/SAN/GLAS/GLA12.034). You can the click and save the files that you need. I however needed to sort out a bulk download - this is where using an [FTP](http://en.wikipedia.org/wiki/File_Transfer_Protocol) client comes in handy such as [WinSCP](http://winscp.net/eng/index.php).

However, I found it much simpler - especially as the data was all freely available (i.e. no user or password details requried) - to do this from a terminal. In linux, this can be done directly through bash. In a windows environment, the best approach is to download [cygwin](https://www.cygwin.com/), ensure that you have ["wget" installed](http://superuser.com/questions/693284/wget-command-not-working-in-cygwin) (search the package list as and when you run in the cygwin installation .exe). Then all you'll need to type is:

{% highlight bash %}
> wget -P ~/your_output_folder_destination -m ftp://the_url_of_the_ftp_site/*
{% endhighlight %}

In the above snippet "-P" is allowing you to specify where you want to put the data you are acquiring and "-m" allows a recursive download of the specified URL. Get all of that running and leave it in the background to complete and you're done!
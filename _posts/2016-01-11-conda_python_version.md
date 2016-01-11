---
layout: post
title: Changing your Python version with Anaconda
categories: Python			
tags: python version anaconda
---

Python 3 is the future and the future is now. Considering best practise, the way forwards is to move with the times and upgrade. HOWEVER, when all of your scripts are written in a Python 2.x way, maybe now isn't the time to move on... having a load of v2.x / v3.x errors can be inconvenient to say the least. 

I'm not saying that you should, I'm simply showing how you could downgrade your python version if using [Anaconda](https://www.continuum.io/downloads).

Downgrading between versions is easy if you are using an Anaconda Python distrib. By going on to the command line, it is possible to quickly search for available versions and upgrade/downgrade accordingly.

# Step-by-step downgrade/upgrade

**************************
FOR MORE OFFICIAL INFO READ [HERE](http://conda.pydata.org/docs/py2or3.html) 
**************************

1. Open up your terminal
2. Search for available versions - can search for what you want, but we'll look for "python"
	
		> conda search python

		which returns something like this:

		Fetching package metadata: ....
		ipython                      0.13                     py27_0  defaults        
		                             0.13.1                   py27_0  defaults        
		                             0.13.1                   py26_0  defaults        
		                             0.13.1                   py33_1  defaults        
		                             0.13.1                   py27_1  defaults        
		                             0.13.1                   py26_1  defaults        
		                             0.13.2                   py33_0  defaults             

		                            ....

		ipython-notebook             0.13.2                   py27_0  defaults        
		                             1.0.0                    py27_0  defaults        
		                             1.1.0                    py33_0  defaults        
		                             1.1.0                    py27_0  defaults        

		                            ....

		python                       2.6.8                         5  defaults        
		                             2.6.8                         6  defaults        
		                             2.6.9                         0  defaults        
		                             2.6.9                         1  defaults        
		                             2.7.3                         2  defaults        
		                             2.7.3                         3  defaults        
		                             2.7.3                         4  defaults        
		                             2.7.3                         5  defaults        
		                             2.7.3                         6  defaults        
	                                 
	                                 ....

		                             2.7.8                         0  defaults        
		                             2.7.9                         0  defaults        
		                          *  2.7.9                         1  defaults        
		                             2.7.10                        0  defaults        
		                             2.7.10                        1  defaults        
		                             2.7.10                        3  defaults        
		                             2.7.10                        4  defaults        
	                             	 
	                             	 ....
		                             
		                             3.4.3                         5  defaults        
		                             3.5.0                         0  defaults        
		                          .  3.5.0                         1  defaults        
		                             3.5.0                         2  defaults        
		                             3.5.0                         3  defaults        
		                             3.5.0                         4  defaults        
		                             3.5.1                         0  defaults        

3. To change your python version, you can now just type:
	
		conda install python=3.5.0

		# or maybe 

		conda install python=2.7.8

		# or whatever you want....


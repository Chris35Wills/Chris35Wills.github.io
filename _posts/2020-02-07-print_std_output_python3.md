---
layout: post
title: Print to file from standard output using Python 3
categories: Python, IO, text
---

To print standard output to a file in python 3, you can make use of the `redirect_stdout` function from the `contextlib` pacakge. The following example uses this library to write the standard output printed from a function to a text file with some header info. Feel free to adapt it to your use case.

```python
from contextlib import redirect_stdout

# define your output file name and location
ofile="your/output/file.txt"

def printer(some_value):
	"""
	Arbitrary function that prints stuff to standard output
	
	some_value - a value you want to print (will be converted to int)
	"""
	print("-------------------------")
	print("Score: %i" %(int(some_value)))
	print("  ")
	print("LEX-RCS")
	print("  ")
	
# Write to file
with open(ofile,'w') as out:
	with redirect_stdout(out):
		print("This will be the header of the file")
		print("-------------------------")
		print(" ")
		printer('2')
		printer('3')
		printer('4')
```		
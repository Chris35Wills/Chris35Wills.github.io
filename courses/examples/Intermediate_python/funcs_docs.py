"""
Some simple functions to make repeat operations faster.
"""

__author__ = "A. Person"
__email__ = "aperson@web.net"

def subtract(a,b):
	"""subtracts b from a and retuns the answer"""

	c=a-b

	return c


def summate(a,b):
	"""sums together a and b and retuns the answer"""

	c=a+b

	return c


def sumKM(a,b):
	"""sums together a and b, divides by 1000 and retuns the answer"""
	
	c=(a+b)/1000.

	return c


def minusX10(a,b):
	"""subtracts b from a, multiplies by 10 and retuns the answer"""
	c = (a-b)*10

	return c


def divAdd5(a,b):
	"""divides a by b, adds 5 and retuns the answer"""

	c = (a/b)+5

	return c


if __name__ == "__main__":
	print("Run from import")
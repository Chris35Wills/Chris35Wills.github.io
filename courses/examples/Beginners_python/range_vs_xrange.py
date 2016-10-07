a = range(1,11,2) # returns a list
b = xrange(1,11,2) # creates an xrange object (not a list) << better for long number genration

for i in a:
	print(i)

print("Now with xrange:")
for i in xrange(1,11,2):
	print(i)
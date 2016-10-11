##################
# a nice overview: http://www.physics.nyu.edu/pine/pymanual/html/chap3/chap3_arrays.html

# list is a collection of different elements

l = []
type(l)
l.append("this")
l.append("and")
l.append("that")
l.append(2)
len(l)
l[2] # access parts of list
l[1:3] # slice the list
l[::-1] # read list backwards

l2 = ["other", "bits"]
l_all = l + l2 # concatenate lists

# range returns a list

nums = range(0,11,2)
type(nums)
len(nums)

##################
# tuple

# a list that cannot be changed once it has been created (immutable)
# created and accessed as a list but cant be changed!

t = (1,2,3,4,5)
type(t)
t[1]
t[1:3] # slice like a list
t[::-1] 
t[1]=3 # fails as you aren't allowed to change it!

#############
# arrays are a numpy thing!
# lists are often referred to (incorrectly) as arrays but they are different

import numpy as np

a=np.array([1,2,3,4])
type(a)
a. # see funcs
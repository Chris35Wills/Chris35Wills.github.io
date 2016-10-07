import sys

n_arguments = len(sys.argv)

for i in range(0, n_arguments):
    print("Argument %d equals %s" % ( i, sys.argv[i] ))
    
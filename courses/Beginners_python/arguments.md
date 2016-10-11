---
---

# Arguments!

Arguments are important for all programs. Arguments for programs have nothing to do with shouting, but are additional bits of information supplied to the program when it is run. Open a new Python script `nano arguments.py` and type this;

```python
import sys

n_arguments = len(sys.argv)

for i in range(0, n_arguments):
    print("Argument %d equals %s" % ( i, sys.argv[i] ))
```

Run this script by typing

    python arguments.py here are some arguments

What do you see? Can you work out what happened?

In this case you passed four arguments to your script; `here`, `are`, `some` and `arguments`. The Python interpreter read those arguments and placed them, together with the name of the script, into a special variable called `sys.argv` that you can access from your script (the `sys.argv` variable comes from the module called `sys`. This is why we have to load (`import`) the `sys` module at the start of the script using the line `import sys`).

Because there can be more than one argument, the `sys.argv` variable must be capable of holding more than one value. `sys.argv` must be able to hold multiple values. Arrays are variables that can hold multiple values. A list is a collection of values that can be accessed by their index. Create a script list.py and write this;

```python
from __future__ import print_function

my_list = [ ]

my_list.append( "cat" )
my_list.append( "dog" )
my_list.append( 261 )

print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])

print("my_list contains %d items" % ( len(my_list) ))

another_list = [ 1, 2, 3, "purple", 51.2 ]

print(another_list[4])

two_dimensional_list = [ [1,2,3], [4,5,6], [7,8,9] ]

print(two_dimensional_list[0][2])

for i in range(0, 3):
    for j in range(0,3):
        print("%d " % (two_dimensional_list[i][j]), end="")

    print("\n", end="")
```

Run this script `python list.py`. Can you understand what has been printed and why?

The size of an list (the number of values it contains) can be found by typing `size_of_list = len(list)`. You can access an individual value within the list using square brackets, e.g. `list[0]` is the first value in the list, `list[1]` is the second value etc. (Note that we start counting from zero - the first item is at `list[0]` not `list[1]`).

***

## Exercise

Use the knowledge you've gained so far to write a Python script that can print out any times table. Call your script times_table.py, and have it read two arguments. The first argument should be the times table to print (e.g. the five times table) while the second should be the highest value of the times table to go up to. So

    python times_table.py 5 12

should print the five times table from 1 times 5 to 12 times 5.

Note that the arguments are loaded into Python as strings. You will need to convert them to integers by using the lines like;

```python
n = int( sys.argv[1] )
```

[Answer](../arguments_answer1) (don't peek at this unless you are stuck or until you have finished!)

As an extension, can you think of a way to use lists to print out the times table using words rather than using numbers? To do this you will need to know that you can assign values to an list using the following syntax;

```python
a = [ 1, 2, 3, 4, 5 ]
b = [ "cat", "dog", "fish", "bird" ]
c = [ "zero", "one", "two", "three" ]
```

[Answer](../arguments_answer2) (don't peek at this unless you are stuck or until you have finished!)

# [Previous](../loops) [Next](../conditions)

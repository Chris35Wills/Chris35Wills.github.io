---
---

# Running Programs

So far you've seen how you can use Python to process your output files. However, what makes Python a good glue language is its ability to actually run programs as well. There are several ways to run a program from your Python script. I'll only present a couple of ways here. Open a new Python script (`nano system_run.py`) and copy the following;

```python
import sys
import subprocess

directory = sys.argv[1]

subprocess.call( "ls %s" % directory, shell=True)
```

This is a simple script that just lists the contents of a directory. The key line is `subprocess.call("ls %s" % directory)`. The system command (part of the os module) is passed a string, and executes the value of that string in pretty much exactly the same way that the same text would have been executed if you had typed it yourself at the command line. The output of the command is printed to the screen.

`subprocess.call` is good if you want to just run a program. However, there are times when you would like to process the output of the program within Python. To do this, you have to use `subprocess.Popen`. Open a new Python script (`nano popen.py`) and copy the following;

```python
import sys
import subprocess

directory = sys.argv[1]

# Ask your computer to run the 'ls' command on the specified directory.
# This is the important line.
files = subprocess.check_output("ls %s" % directory, shell=True)

# The rest of this is just formatting the output of the system call...

# check_output returns a 'bytestring'. We need to convert this to a string 
# format that we can understand:
files = files.decode('utf8')
# And then, specific to the 'ls' command, we need to do some formatting.
# First strip any trailing space from the bottom/right of the string
files = files.rstrip()
# And then split the string of files into a list:
files = files.split('\n')
# Finally we can now see how many files are available:
nfiles = len( files )

print("There are %d files in %s" % (nfiles, directory))

# Loop through the list of files
for i in range(0, nfiles):
    print("%d: %s" % ( i, files[i] ))
```

This script lists the contents of a directory, but first says how many files are in the directory, and then prints each one preceded by its number.

The key line here is `files = subprocess.Ppopen( "ls %s" % directory, "r" )`. The string contained in the string `"ls %s" % directory` is executed, and returned as a virtual filehandle. Like normal filehandles, you can get all of the lines by using the `readlines` function. Note that the newline (`\n`) character is left on the end of each output line. Use the `rstrip()` command if you want to remove the newline character, e.g. `files[i].rstrip()`.

**Note:** If you just want to get a list of files using Python, there is a much simpler way, as follows:

```python
from glob import glob
import sys

directory = sys.argv[1]

# Look inside the directory. The * denotes search for all items within this
# directory.
files = glob(directory + '/*')

# Do some formatting like above.
nfiles = len(files )
print("There are %d files in %s" % (nfiles, directory))
for i in range(0, nfiles):
    print("%d: %s" % ( i, files[i] ))
```


***

## Exercises

`convert` is a UNIX program that can convert an image from one file format to
another (e.g. convert a JPEG file to a PNG). Write a Python script that can convert 
all of the JPEG files in a directory into PNG files.

(the command to convert `file.jpg` to `file.png` is `convert file.jpg file.png`)

[Here's a possible answer](../running_answer).

# [Previous](../replacing) [Next](../jobs)

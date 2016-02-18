#Running Programs Answer to exercise 1

```python
import sys
import os
import re

directory = sys.argv[1]

jpeg_files = os.popen( "ls %s/*.jpg" % directory, "r" ).readlines()

for jpeg_file in jpeg_files:
    jpeg_file = jpeg_file.rstrip()

    png_file = re.sub( r"jpg$", "png", jpeg_file )

    command = "convert %s %s" % (jpeg_file, png_file)

    print "Running '%s'..." % command

    os.system( command )
```

***

[Compare with Perl](../beginning_perl/running_answer.md)

***

# [Previous](running.md) [Up](README.md) [Next](running.md)

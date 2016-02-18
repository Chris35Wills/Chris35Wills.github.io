#Splitting Lines Answer to exercise 1

```python
import sys

lines = open( sys.argv[1], "r" ).readlines()

nlines = 5

if nlines > len(lines):
    nlines = len(lines)

for i in range(0, nlines):
    words = lines[i].split()

    if len(words) > 0:
        print(words[0])
```

***

[Compare with Perl](../beginning_perl/splitting_answer1.md)

***

# [Previous](splitting.md) [Up](README.md) [Next](splitting.md)

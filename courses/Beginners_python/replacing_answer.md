---
---

```python
import sys
import re

search_string = sys.argv[1]

replace_string = "**%s**" % ( search_string.upper() )

lines = open( sys.argv[2], "r" ).readlines()

for line in lines:
    print( re.sub( search_string, replace_string, line ) )
```

# [Previous](../replacing) [Next](../replacing)

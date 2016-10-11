---
layout: post
title: Test python package versions within a module
categories: python, test
tags: python test
---

Testing python package versions is possible using the standard python package [distutils](https://docs.python.org/2.7/library/distutils.html):

```python
from distutils.version import StrictVersion
import numpy as np
import sys

if not (np.version.version>=StrictVersion('1.8.0')):
	sys.exit("Update numpy to at least version 1.8.0")
```

If you have a module with a __init__.py file, stick something like the above in that file and on import, if the version available is incorrect, you'll get an error e.g.

```python
An exception has occurred, use %tb to see the full traceback.

SystemExit: Update numpy to at least version 1.8.0
```
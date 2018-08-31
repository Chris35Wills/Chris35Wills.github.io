---
layout: post
title: List comprehensions - some examples (Python 3.x)
categories: Python
---

I've recently been using list comprehensions more often than not, having never paid them much attention. A decent overview is available [here](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python).
Perhaps they are a sprinkling of [syntactic sugar](https://stackoverflow.com/questions/30096351/are-list-comprehensions-syntactic-sugar-for-listgenerator-expression-in-pyt) but I think I'm a fan.

Here are a few more (increasingly nuanced) examples you might find helpful. The only import we need is `os`:

Make a couple of lists:

```python
list_0=[1,2,3,4,5]
```

Iterate through each element of list:

```python
[i for i in list_0]
```

Make a couple of lists with a path:

```python
list_1=['W:/some_path/file1.txt','W:/some_path/file2.txt', 'W:/some_path/file3.txt']
list_2=['W:/some_other_path/file1.txt', 'W:/some_path/file2.txt']
```

Get file name for each element in list:

```python
[os.path.basename(i) for i in list_1]
[os.path.basename(i) for i in list_2]
```

Get directory name for each element in list:

```python
[os.path.dirname(i) for i in list_1]
[os.path.dirname(i) for i in list_2]
```

Get elements in list_1 not in list_2:

```python
[x for x in list_1 if x not in list_2]
```

Get elements in list_2 not in list_1:

```python
[x for x in list_2 if x not in list_1]
```

Get unique file regardess of path and keep only unique files WITH their original path (thanks to [this answer](https://stackoverflow.com/questions/41028547/python-using-list-comprehensions-to-filter-a-list-by-a-list-of-substrings/41028575)):

```python
[r for r in list_1 if not any(os.path.basename(z) in r for z in list_2)] 
```

Create list of file names using a pre-formatted output file name:

```python
output_areas=('A','B','C','d','e')
["%s_summary.csv" %(i) for i in output_areas] 
["%s_summary.csv" %(i.upper()) for i in output_areas] # all upper case
["%s_summary.csv" %(i.lower()) for i in output_areas] # all lower case
```
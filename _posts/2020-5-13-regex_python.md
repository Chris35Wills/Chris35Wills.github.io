---
layout: post
title: Using regex to select elements of a string with python
categories: python
---

Imagine you have a list of string elements, such as you might get after reading in a text file line by line that looks as follows:

```python
data=['month::5-->', 'day::13-->']
```

From the above, it looks like a value is provided between some label e.g. `month::` and an end string e.g. `-->`. If for example you wanted to get at the `month` part, you could access it as follows from which point you could start messing around with splitting etc:

```python
list(filter(lambda k: 'month::' in k, data))
>>['month::5-->']
```

Say your data looks like the following though as the file contained some unexpected gaps:
  
```python
data=['address::1, Humpty Dumpty Lane,', 'Somewhere -->', 'month::5-->', 'day::13-->']
```
 
Notice how the strings that were bordering the info are different list elements now? 

```python
data[0]
>>'address::1, Humpty Dumpty Lane,'

data[1]
>>'Somewhere -->'
```

If I want to get the address, I could try the `filter` approach but it won't get everything I need as really I need it to continue up to the `-->` which is now in a different list element:

```python
list(filter(lambda k: 'address::' in k, data))
>> ['address::1, Humpty Dumpty Lane,']
```

A more efficient and tidy way to deal with this is to use regular expressions through the `re` package. First, concatenate everything into a string:

```python
all_content=' '.join(data) 
```

Now use the following:

```python
import re

address_info=re.findall("address::(.*?)-->", all_content)

print(address_info) # the list
>>['1, Humpty Dumpty Lane, Somewhere']
print(address_info[0]) # the string
>>1, Humpty Dumpty Lane, Somewhere
```

This looks for the first instance of `address::`, then with `(.*?)` gets all text up to the first instance of `-->`. If you just pass `(.*)` it will be *greedy* and get all text up to the last occurrence of `-->` which matters if you have a few of them!

For help with finding and testing regex commands, check out [pythex](https://pythex.org/). You can see it working with the example provided [here](https://pythex.org/?regex=address%3A%3A(.*)--%3E&test_string=address%3A%3A1%2C%20Humpty%20Dumpty%20Lane%2C%20Somewhere%20--%3E&ignorecase=0&multiline=0&dotall=0&verbose=0).

Thanks John Stevenson for the help!

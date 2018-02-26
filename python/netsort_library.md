# natsort python library
natsort is a python package to provide some kinds of sort function.
# Motivation
Python's built-in `sorted()` sorts array something wrong sometimes.<br>
For example,
```python
data = [1,10,3,2,200,4,5]
print(sorted(data))
```
It outputs `[1,10,2,200,3,4,5]`. But I wanted to sort like `[1,2,3,4,5,10,200]`.<br>
`natsorted()` enables us to sort like that.
# Usage
```python
import natsort as ns
data = [1,10,3,2,200,4,5]
print(ns.natsort(data))
```
# Reference
**[Link](https://pypi.python.org/pypi/natsort)**

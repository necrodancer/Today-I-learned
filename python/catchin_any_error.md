# Catching any error exception in `try:` and `except:`
By using `traceback` and `logging` module, you can catch general errors as exception.

Let's assume a function `zero_index()` returns 1st element of a list.

If you feed non-list input such as integer, it will produce an error.

Let's catch error with `logging.error(traceback.format_exc())`.
```python
import traceback
import logging

def zero_index(arr):
    return arr[0]

try:
    a = [1]
    b = 1
    print("a:", zero_index(a))
    print("b:", zero_index(b))
except Exception as e:
    logging.error(traceback.format_exc())
```

And the output is
```
ERROR:root:Traceback (most recent call last):
  File !@!#%%@%#@$, line 11, in <module>
    print("b:", zero_index(b))
  File !@!#%%@%#@$, line 5, in zero_index
    return arr[0]
TypeError: 'int' object is not subscriptable

a: 1
```

As you can see the function `zero_index` successfully returns `a[0]` not `b[0]`.

For `b`, error log catched `TypeError`.

# Reference
[About catching ANY exception](https://stackoverflow.com/questions/4990718/about-catching-any-exception)

# Creating a directory if it does not exist
When you create a directory,
this code helps you. <br>
I just take a note this code to remember and refer. <br>
```python
import os

if not os.path.isdir(new_path):
    os.makedirs(new_path)
```

# Reference
[Python os.makedirs\(\) Examples](https://www.programcreek.com/python/example/38/os.makedirs)

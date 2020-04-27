# Creating nested directory
Python module `pathlib` works for creating nested directories from its method `mkdir` with `parents=True` and `exist_ok=True`.
```python
# Create directories
from pathlib import Path
Path("./NewDirectory/Image/JPEG/Class1").mkdir(parents=True, exist_ok=True)
Path("./NewDirectory/Image/JPEG/Class2").mkdir(parents=True, exist_ok=True)
Path("./NewDirectory/Image/JPEG/Class3").mkdir(parents=True, exist_ok=True)
Path("./NewDirectory/Label/Class1").mkdir(parents=True, exist_ok=True)
Path("./NewDirectory/Label/Class2").mkdir(parents=True, exist_ok=True)
Path("./NewDirectory/Label/Class3").mkdir(parents=True, exist_ok=True)

# Print directories
import os
for parent, children, _ in os.walk('./NewDirectory'):
    print(parent)
```

Result of print:
```
./NewDirectory
./NewDirectory/Image
./NewDirectory/Image/JPEG
./NewDirectory/Image/JPEG/Class1
./NewDirectory/Image/JPEG/Class3
./NewDirectory/Image/JPEG/Class2
./NewDirectory/Label
./NewDirectory/Label/Class1
./NewDirectory/Label/Class3
./NewDirectory/Label/Class2
```
# Reference
Check the [stackoverflow](https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory).

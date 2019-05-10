# Rename forlders using `os` module
```python
count = 0
for old_name in os.listdir(base_path):
    new_name = oldname+str(count)
    os.rename(os.path.join(base_path, old_name),
          os.path.join(base, new_name))
    count += 1
```
This code derives from [here](
https://stackoverflow.com/questions/8735312/how-to-change-folder-names-in-python
). <br>

# Reference
[How to change folder names in python?](
https://stackoverflow.com/questions/8735312/how-to-change-folder-names-in-python
)

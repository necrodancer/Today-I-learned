# Filtering keyword-strings in a python list
```python
a = [
    'Apple/Banana',
    'Apple/Pear',
    'Orange/Blueberry',
    'Orange/Tomato'
]
keywordFilter= ['Apple','Tomato']  # you can add multiple keywords to avoid
filtered = [string for string in a if not any(word in string for word in keywordFilter)]
print(filtered)
```
So output is:
```
['Orange/Blueberry']
```

# References
[Python: Remove the certain string from list if string includes certain keyword](https://stackoverflow.com/questions/28565920/python-remove-the-certain-string-from-list-if-string-includes-certain-keyword)

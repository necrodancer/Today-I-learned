# Python regular expression
## Extract Korean, numbers, and alphabets.
```python
# python regular expression example
# extract 'Korean number ALphabet'
path_list = [
    './Folder/안녕 1234 AB',
    './Folder/하세 5678 CD',
    './Folder/요 9101112 EF',
            ]

import re
# template: (Alphabet,Korean,'-',' ')(numbers)(Alphabet,' ')
template = re.compile("([a-zA-Zㄱ-ㅣ가-힣\- ]+)([0-9]+)([a-zA-Z ]+)")  

for path in path_list:
    p = path.split('/')[-1]
    print(p)
    processed = template.match(p).groups()
    print(processed)
```

## Explanation
`re` module allows python expression to extract strings with my own template, such as `template` in the above code.

Define an template using `re.compile('([stuffs]+)([stuffs]+)...')`.

For the `stuffs`, you can type `a-zA-Z` for English.

Also you can try `0-9` for integers. Finally you can specify the range of Korean like `ㄱ-ㅣ가-힣`.

More information is referred to References.

Finally, you can make a group by using `template.match(string).groups()`.

It will return a tuple of strings like:
```
안녕 1234 AB
('안녕 ', '1234', ' AB')
하세 5678 CD
('하세 ', '5678', ' CD')
요 9101112 EF
('요 ', '9101112', ' EF')
```

# References
1. [Python | Splitting Text and Number in string](https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string/)
2. **[Splitting Korean and Number](https://stackoverflow.com/questions/54761816/splitting-korean-and-number)**

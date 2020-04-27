# How to read text lines in Python
```python
DIR = './test.txt'
f = open(DIR, mode='r')

# Deal with line by line using f.readlines()
for line in f.readlines():
    print(line)

```
Alternative:
```python
DIR = './test.txt'
lines = open(DIR, mode='r').read().splitlines()  # it not only removes '\n' but also directly returns a list of text lines.

for line in lines:
    print(line)
```

# References
1. [Python(파이썬) 기본 - 47. 파일 - 텍스트 파일 다루기](https://suwoni-codelab.com/python%20%EA%B8%B0%EB%B3%B8/2018/03/12/Python-Basic-file/)
2. [Python – remove newline from readlines](https://viewsby.wordpress.com/2014/08/28/python-remove-newline-from-readlines/)

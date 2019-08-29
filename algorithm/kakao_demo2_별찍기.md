# Problem
Print `m`x`n` rectangle with `*` for given input `n` and `m`.

# Solution
Get input of `n` and `m`, and generate `for` loop for 'm'.

In the loop, print `*` with `m` times.

# What tackled me


# Source code
Written in Python 3.

```python
n, m = map(int, input().strip().split(' '))

for i in range(0,m):
        print("*"*n)
```

# What I learned
`<string>.strip()` removes blank from the start and end.

`<string>.split(<condition>)` splits the string into lists with the `<condition>` such as ' ', ',', and '-'. The default condition is ' '.


# Future challenges

# Reference
1. [02-2 문자열 자료형](https://wikidocs.net/13#strip)

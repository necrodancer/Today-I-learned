# Get indices of ordering
For given list of numbers, 
you might the rankings of not sorted numbers. <br>
If elements are unique,
```python
x = [4, 7, 9, 10, 6, 11, 3]
seq = sorted(x)
index = [seq.index(v) for v in x]
```
# Reference
[
Creating a list containing the rank of the elements in the original list
](
https://codereview.stackexchange.com/questions/65031/creating-a-list-containing-the-rank-of-the-elements-in-the-original-list
)

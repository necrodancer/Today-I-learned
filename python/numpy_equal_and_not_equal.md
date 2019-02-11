# Numpy `equal` and `not_equal`
Sometimes, you need to compare arrays elementwisely.<br>
`np.equal` and `np.not_equal` permforms it well.
# np.equal()
```python
>>> np.equal([0, 1, 5], np.arange(3))
array([ True,  True, False], dtype=bool)
```
# np.not_equal()
```python
>>> np.not_equal([1.,4.], [1., 5.])
array([False,  True], dtype=bool)
>>> np.not_equal([1, 4], [[1, 6],[1, 8]])
array([[False,  True],
       [False,  True]], dtype=bool)
```
# Reference
[numpy.equal](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.equal.html#numpy.equal) <br>
[numpy.not_equal](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.not_equal.html#numpy.not_equal)

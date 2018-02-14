# np.random.normal
Draw random samples from a normal(Gaussain) distribution.<br>
It returns ndarray or scalar; drawn samples from the paramterized normal distribution.
# Format
```python
numpy.random.normal(
    local=0.0,   # mean(centre) of distribution 
    scale=1.0,   # standard deviation (spread or width) of the distribution
    size=None    # int or tuple; optional. Output shape. e.g. (m,n,k) == m*n*k, None == single value
    )
```
# Example
```python
centre = 0
std = 0.01
value = np.random.normal(centre, std, 1) # It returns single value.
```

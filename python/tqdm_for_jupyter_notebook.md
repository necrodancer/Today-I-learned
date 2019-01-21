# tqdm for jupyter notebook
`tqdm` is a module to support progress bar in python console. <br>
Usually, it can be applied like this:
```python
from tqdm import tqdm

pbar_length = 20
pbar = tqdm(total=pbar_length)
for i in range(0,20):
    pass
    pbar.update(1)
pbar.close()
```
# In jupyter notebook
`tqdm` is useful, but it sometimes prints multiple progress bar in the jupyter notebook. <br>
To solve this problem, `tqdm` provides `tqdm_notebook`. <br>
Just import like this:
```python
from tqdm import tqdm_notebook as tqdm
```

# Reference
[tqdm in Jupyter Notebook](https://stackoverflow.com/questions/42212810/tqdm-in-jupyter-notebook)

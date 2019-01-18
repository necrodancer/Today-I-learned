# Prevent plot from showing in jupyter notebook
```python
fig= plt.figure()
plt.plot(range(10))
fig.savefig("save_file_name.pdf")
plt.close()
```

# Reference
[Prevent plot from showing in jupyter notebook](https://stackoverflow.com/questions/18717877/prevent-plot-from-showing-in-jupyter-notebook)

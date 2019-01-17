# Removing margins from pyplot.imshow()
This code is to remove margins from pyplot.AxesImage genereated from pyplot.imshow(). <br>
In the end, pyplot.AxesImage is saved without plotting the image in the jupyter notebook. <br>
```python
figure = plt.figure(figsize=(5,5))
fig = plt.imshow(numpy_array, aspect='auto', cmap='jet')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.axis('off')
file_name = fname +'.png'
file_path = os.path.join(directory,file_name)
plt.savefig(file_path, bbox_inches = 'tight', pad_inches = 0)
plt.close()
```
From this code, still a thin margins remain. I don't know how to remove. <br>
# Reference
[Removing white space around a saved image in matplotlib](https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib)

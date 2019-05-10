# Matplotlib custom colormap
Sometimes, you may need your custom colormap to plot a image using matplotlib. <br>
Thankfully, [the official document of matplotlib]
(
https://matplotlib.org/tutorials/colors/colormap-manipulation.html
)provides some codes to define the custom colormap. <br>
One of them, you can concatenate two kinds of colormaps that are already defined in matplotlib : <br>
```python
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

top = cm.get_cmap('Reds_r', 128)
bottom = cm.get_cmap('Blues', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')
```
There are existing colormaps [here](
https://matplotlib.org/tutorials/colors/colormaps.html
). You can refer these colormaps <br>

# References
[Choosing Colormaps in Matplotlib](https://matplotlib.org/tutorials/colors/colormaps.html)
[Creating Colormaps in Matplotlib](https://matplotlib.org/tutorials/colors/colormap-manipulation.html)

# keras.backend.squeeze
This method reduces a channel which you want to remove.<br>
# Example
```python
from keras.layers import Lambda
import keras.backend as K

# ...
outt = Lambda(lambda x:K.squeeze(x,axis=0))(inn) # it removes 1st channel(axis=0) of 'inn'.
```
# Reference
[Keras backends](https://keras.io/backend/)

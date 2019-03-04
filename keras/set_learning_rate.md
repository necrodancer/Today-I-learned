# Set learning rate in Keras
Except for loss definition and model.compile(), <br>
Sometimes, we need to put learning rate manually. <br>
Here is example. It uses keras backend. <br>
```python
from keras import backend as K
# To get learning rate
print(K.get_value(model.optimizer.lr))
# To set learning rate
K.set_value(model.optimizer.lr, 0.001)
keras.__version__ # 2.0.2
```
# Reference
[Using keras to load model and assign new values to its parameters](https://stackoverflow.com/questions/47523841/using-keras-to-load-model-and-assign-new-values-to-its-parameters)

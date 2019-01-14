# Slicing array channels with keras.layers.Lambda
For example, slicing only 2nd channel of input:
```python
y = Lambda(lambda x: x[...,2])(x)
```
Since keras model should be connected with only keras.layers class, <br>
slicing operation like x[...,2] should be wrapped with keras.layers.Lambda. <br>

# Reference
[Are there slice layer and split layer in Keras? #890](https://github.com/keras-team/keras/issues/890)

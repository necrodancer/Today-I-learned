# keras.layers.Lambda

wrapping arbitrary function as `Layer` object.

\* Notice: Every keras layer should be `Layer` object when they are connected to one anohter. So, `Lambda` layer enables non-Layer function to be Layer object to be part of a neural network.

# Usage
```python
# functional expression
y = keras.layers.Lambda(lambda x: x[:1])(x)

# in the Sequential
model.add(keras.layers.Lambda(lambda x: x**2))
```

# Special usage
```python
y = keras.layers.Lambda(lambda x: keras.backend.switch(cond, 
                          lambda: keras.layers.GRU(units,return_sequences=True)(x), 
                          lambda: keras.backend.zeros(shape=(1,time_steps,units))))(seq)
```
This code is from [Apply LSTM to each matrix element with Keras](https://datascience.stackexchange.com/questions/63848/apply-lstm-to-each-matrix-element-with-keras).

This code uses multiple built-in `lambda` in the `Lambda` layer.

[tf.keras.backend.switch](https://www.tensorflow.org/api_docs/python/tf/keras/backend/switch) allows that if `condition` is true, execute `function1`, else execute `function2`.

So, if `cond` is satisfied, GRU will be used, otherwise zeros will be executed. 

And the input of `Lambda` is `seq`. That's it. 

# References
* https://keras.io/ko/layers/core/
* https://www.tensorflow.org/api_docs/python/tf/keras/backend/switch
* https://datascience.stackexchange.com/questions/63848/apply-lstm-to-each-matrix-element-with-keras

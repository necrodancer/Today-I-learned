# InvalidArgumentError: 0 is duplicated in the input.
This error happens when you don't feed input to tensorflow op such as `optimizer` or `train_step`.<br>
So, the input should be feeded. <br>
# Example
```python
from keras.layers import Input
from keras.models import Model
inn = Input(shape=(8,8))
# ...
model = Model(inputs=inn, outputs=outt)
# below is tensorflow loop not model.fit() from keras
sess.run(train_step, feed_dict={sth:sth_array,
                                inn:train_x,
                                # ...
})
```

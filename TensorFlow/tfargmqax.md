# tf.argmax
### tf.argmax
tf.argmax() is a method provided from Tensorflow.<br>
It returns indices of max value for each axis.<br>
Actually I don't understand what axis is. So after studying this, this document will be updated.
### references
[Tensorflow document](https://www.tensorflow.org/api_docs/python/tf/argmax) <br>
[Koeran explanation](http://pythonkim.tistory.com/73)
<br>
<br>
<br>
### Example code
```python
import tensorflow as tf

a = tf.Variable([[3., 1., 0.],[2., 0., 5.]])
b = tf.Variable([[[1., 2., 3.],[0., 5., 2.]]])

y = tf.argmax(a, axis=0)
z = tf.argmax(a, axis=1)
i = tf.argmax(b, axis=0)
j = tf.argmax(b, axis=1)
k = tf.argmax(b, axis=2)

sess =tf.Session()
sess.run(tf.global_variables_initializer()) # if you do not initialize, it may raise an error.
print(sess.run(y))
print(sess.run(z))
print(sess.run(i))
print(sess.run(j))
print(sess.run(k))
```

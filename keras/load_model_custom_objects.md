# When load_model() says global name 'oo' is not defined
When you used some kinds of global name during defining model, <br>
It can cause error like `global name 'oo' is not defined`. <br>
At that time, you can use `custom_objects={"oo": oo}` argument in the `load_model()`.<br>
For example,<br>
```python
load_model("model_path", custom_objects={"tf": tf})
```
# Reference
[Keras model cannot be loaded if it contains a Lambda layer calling tf.image.resize_images #5298](https://github.com/keras-team/keras/issues/5298)

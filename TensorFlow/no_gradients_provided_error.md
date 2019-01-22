# No gradients provided for any variable ?
I encoutered this error when I implemented `loss` and `optimizer` like this:
```python
loss = my_custom_loss(y_pred,y_true)
loss_container = tf.placeholder(tf.float32)
optimizer = tf.tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss_container)
# ...
    sum_loss = []
    for i in range(0,batch):
        cur_loss = sess.run(loss, ...)
        sum_loss += cur_loss
    sess.run(optimizer,feed_dict={loss_container:sum_loss/batch})
```
Then the error `No gradients provided for any variable ?` occured.<br>
Now I know the graph was definitely disconnected. <br>
To avoid this kinds of error, you should connect loss and optimizer directly:
```python
loss = my_custom_loss(y_pred,y_true)
optimizer = tf.tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(loss)
```
If you want to iterate loss operation and merge them, just create `tf.concat` node, <br>
and run that node and loss node multiple times. And then define final loss like this:
```python
final_loss = tf.reduce_mean(concatanated)
optimizer = tf.tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(final_loss)
```

# Numpy one-hot encoder
### One-hot encoding
One-hot encoding is encoding a decimal number to a vector includes only zero and one(it is different from binary number).<br>
For example, if we have 0, 1, 2, they can be encoded like this:<br>
    (1, 0, 0) // 0 <br>
    (0, 1, 0) // 1 <br>
    (0, 0, 1) // 2 <br>
This method is useful for learning neural networks. For supervised learning, we need training data and their targets.<br>
For learning, The decimal or categorical targets are usually encoded to one-hot vector.
### One-hot encoder implemented with Numpy library.
Many deep learning frameworks support the one-hot encoding method, but to understand its principle,<br>
I decided to implement one-hot encoder with numpy library.<br>
I followed **[this link](https://stackoverflow.com/questions/29831489/numpy-1-hot-array)** to study one-hot encoder.<br>
And I defined a method and gave some comments as follows:
```python
import numpy as np

def one_hot_encoding(arr):
    # Make zero matrix.
    # arr.size means # of rows.
    # arr.max means maximum value of one hot encoding.
    #     if you want to encode to 0~2, [1,0,0],[0,1,0],[0,0,1] will be done.
    #     As you can see, the one hot vector size is 3(2+1). When generalizing,
    #     the size of one hot vector can be the maximum value of raw data + 1. 
    one_hot = np.zeros((arr.size,arr.max()+1))
    # Indexing for encoding, and encoding 1 for each index.
    #     arr[m,n] is for 2d matrix. As you can see, it is possible to input m,n as
    #     np.array.
    one_hot[np.arange(arr.size), arr] = 1
    # return one hot encoded vector
    return one_hot
    
# example data
data = np.array([3, 2, 5, 7])
# one hot encoding
one_hot = one_hot_encoding(data)
print("data:",data)
print("one hot encoding:",one_hot)
```
Output : 
```
('data:', array([3, 2, 5, 7]))
('one hot encoding:', array([[ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  1.]]))
```

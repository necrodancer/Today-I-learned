# Tensorflow version problem
# ImportError: libcudnn.so.6: cannot open shared object file: No such file or directory
I deleted and reinstalled tensorflow-gpu, and tested with importing `tensorflow`.<br>
At that time, the error as below was raised:
```
ImportError: libcudnn.so.6: cannot open shared object file: No such file or directory
Failed to load the native TensorFlow runtime.
```
I'm using virtual environment, Ubuntu 16.0.4, CUDA 8.0, cuDNN 6.0.<br> 
### How I solved
I found I mismatched tensorflow version for my CUDA and cuDNN.<br>
Here is [Tested source configurations](https://www.tensorflow.org/install/install_sources#common_installation_problems) for CUDA version check.
My CUDA and cuDNN versions are 8 and 6. They fit on tensorflow 1.2.0.<br>
So I resintalled TF 1.2.0 like this:
```
(venv)user@user$ pip install tensorflow==1.2.0
```
After installation, it worked. 

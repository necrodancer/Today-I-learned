# Intallation python packages with pip for the created anaconda environment & ignoring a specific package when using pip install
## Situation
I recently decided to create new anaconda2 environment. And I wished to install packages with 'requirements.txt'. <br>
I prepared 'requirements.txt' from my previous environment with
```
$ pip freeze > 'requirements.txt'
```
After that I created new environment like this:
```
$ conda create -n myenv python=2.7
```
The argument `-n` is the same as `--name`, `myenv` is the environment name. Finially I set python version as 2.7.<br>
Then, I activated my new env `myenv` and tried to install 'requirements.txt':
```
$ source activate myenv
(myenv) $ pip install -r requirements.txt
```
But the package was not installed in `myenv`. It looked like not using `myenv`'s pip but using global pip. <br>
I also suffered from another issue with:
```
Cannot uninstall 'certifi'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall.
```
I solved two problems and I'm gonna show my solutions.<br>

## Solution
### Intallation python packages with pip for the created anaconda environment [1]
1. Use `which pip`, and get your environment's pip path : 
```
(myenv) username@username-desktop:~$ which pip
/home/username/anaconda2/envs/myenv/bin/pip
```
2. Use the path with `install -r requirements.txt` : 
```
(myenv) username@username-desktop:~$ /home/username/anaconda2/envs/myenv/bin/pip install -r requirement.txt 
```
### Ignoring a specific package when using pip install [2]
1. Add `--ignore-installed` option :
```
/home/username/anaconda2/envs/myenv/bin/pip install -r requirement.txt --ignore-installed <package_name>
```
<br>
Once finished, you can check your python package list with  `piplist`.

## References
\[1\] [Use 'pip install' in the virtual environment created by conda](https://github.com/ContinuumIO/anaconda-issues/issues/1429) <br>
\[2\] ['Uninstalling a distutils installed project' error when installing blockstack](https://github.com/blockstack/blockstack-core/issues/504)

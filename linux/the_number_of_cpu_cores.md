# How to know the number of cpu cores in Ubuntu
1. `nproc` command returns the number of cpu cores
2. `lscpu` command displays detailed information of cpu in your computer.

# When to know
I am currently using deep learning models implemented with Keras. <br>
Keras provides multiprocessing during training models. <br>
With multiprocessing, I can assign the number of cpu cores. <br>
To use the proper number of cpus, those shell commands above is helpful. <br>

# Reference
[How To Find Number Of CPU Cores From Commandline In Linux](https://www.ostechnix.com/find-number-cpu-cores-commandline-linux/) : This post provides more commands about cpus.

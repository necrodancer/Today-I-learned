# cp command
`cp` is copying directies or files from path_A to path_B.<br>
# 'cp : ommiting directory' error
If you face the error that says 'cp : ommiting directory ~', <br>
please add '-r' option like this: <br>
```
$ cp -r <origin_path> <destination_path>
```
`$` is the prompt of terminal. <br>
`-r` option is that if `<origin_path>` is just a 'file', copy the file,<br>
or if  `<origin_path>` is a directory, copy the directory and its subdirectories and files.<br>

# References
### Korean Refs.
1. [cp : ommiting directory](http://ukthe33.tistory.com/entry/cp-%EB%AA%85%EB%A0%B9%EC%8B%9C-%EC%98%A4%EB%A5%98-omitting-directory-directory-name)
2. [Various options of cp command](http://corej21.tistory.com/m/42)

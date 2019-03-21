# SimpleITK ReadImage Error
Error statement : <br>
```
NotImplementedError: Wrong number or type of arguments for overloaded function 'ReadImage'.
  Possible C/C++ prototypes are:
    itk::simple::ReadImage(std::vector< std::string,std::allocator< std::string > > const &,itk::simple::PixelIDValueEnum)
    itk::simple::ReadImage(std::string,itk::simple::PixelIDValueEnum)
```

# Solution
The `file_path` string should be `utf-8` format.<br>
Apply `file_path` to `file_path.encode('utf-8')`.<br>
Please refer to below original solution link. <br>

# Reference
[SimpleITK NotImplementedError](https://www.kaggle.com/c/data-science-bowl-2017/discussion/27770)

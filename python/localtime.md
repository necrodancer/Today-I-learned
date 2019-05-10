# Localtime using `time` module
`time` module is a module to represent time. <br>
When you want to print local time (such as Korea), <br>
```python
import time

now = time.time()
local_time = time.localtime()
time_format = "%Y-%m-%d %H:%M:%S"
time_str = time.strftime(time_format, local_time)
print(time_str)
```
# Reference
[\[Phtyon\] Tip - 지역시간은 time이 아닌 datetime으로 표현](https://brownbears.tistory.com/242)

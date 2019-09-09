# Problem
7. Reverse Integer

https://leetcode.com/problems/reverse-integer/

# Solution
```python
class Solution:
    def reverse(self, x: int) -> int:
        # int to str
        x_str = str(x)
        
        # check sign
        is_sign = False
        if x_str.startswith('-'):
            is_sign = True
            x_str = x_str[1:]
            
        # str to list
        x_list = list(x_str)
        
        # reverse sum
        x_reverse = ''
        for i in range(0, len(x_list)):
            x_reverse += x_list[len(x_list)-1-i] 
            
        # str to int
        if is_sign == True:
            x_reverse = '-'+x_reverse
        x_reverse_int = int(x_reverse)
        
        # check overflow
        if x_reverse_int > (2**31)-1 or x_reverse_int < (-2**31):
            x_reverse_int = 0
            
        # return 
        return x_reverse_int
```
# How I solved
I decided to convert and process integer into string.

I added code to deal with sign character `-`.

I also considered overflow condition in the problem.

# Result
1032 / 1032 test cases passed.

Status: Accepted

Runtime: 40 ms

Memory Usage: 14 MB

Submitted: 16 minutes ago

# Future work
It can be solved with decimal concepts such as 100x1 + 10x2 + 1x3.

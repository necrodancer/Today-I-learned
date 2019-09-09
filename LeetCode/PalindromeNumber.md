# Problem
9. Palindrome Number

https://leetcode.com/problems/palindrome-number/

# Solution
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # keep x
        origin = x
        
        # check sign and positivise
        is_sign = False
        if x < 0:
            is_sign = True
            x = abs(x)
            
        # dissolve number
        dissolved = []
        while x:
            dissolved.append(x%10)
            x = x//10
        if is_sign == True:
            dissolved = ['-']+dissolved
        
        reverse = [i for i in dissolved[::-1]]

        # judge palindrome
        if dissolved == reverse:
            return True
        else:
            return False
```

# Result
Success

Details 

Runtime: 84 ms, faster than 27.91% of Python3 online submissions for Palindrome Number.

Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Palindrome Number.

# What I learned
Palindrome : The word or number which the original is the same as its reverse.

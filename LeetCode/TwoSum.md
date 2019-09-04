# TwoSum
https://leetcode.com/problems/two-sum/
# Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(0, length):
            for j in range(i+1, length):
                is_sum = nums[i] + nums[j]
                if is_sum == target:
                    return [i, j]
                    
# Test case : [2,7,11,15]
# 9
```
# Results
Accepted.

Runtime: 5896 ms, faster than 6.00% of Python3 online submissions for Two Sum.

Memory Usage: 14.6 MB, less than 18.83% of Python3 online submissions for Two Sum.

# TwoSum2
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/
# Solution
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        values = sorted(list(set(numbers)))
        
        answer = []
        is_break = False
        for i in values:
            for j in values:
                is_sum = i + j
                if is_sum == target:
                    answer = [i, j]
                    is_break = True
                    if is_break == True:
                        break
            if is_break == True:
                break
                    
        
        if answer[0] == answer[1]:
            return [numbers.index(answer[0])+1, numbers.index(answer[0])+2]
        else:
            return [numbers.index(answer[0])+1, numbers.index(answer[1])+1]
            
# Test case : [0,0,3,4]
# target : 0
# Answer : [1,2]
```
# Results
Success
 
Runtime: 80 ms, faster than 28.22% of Python3 online submissions for Two Sum II - Input array is sorted.

Memory Usage: 14.4 MB, less than 5.80% of Python3 online submissions for Two Sum II - Input array is sorted.

# What I learned
If you write down conditions of problem and logics, it will be clear to design algorithm.

Breaking nested loop : Double loop doesn't allow to escape with only one break. I refered here : [here](https://gomguard.tistory.com/190).

`list.index()` returns the 'first' index which you are looking for.

# Problem
Find x and y coordinates for given 3 coordinates to complete an rectangle.

# Solution
Return unique coordinates for each x and y from 3 coordinates.

# What tackled me
I figured out returning unique values already.

But I was confused how to specify x and y coordinates.

So I refered a solution not the code but the idea from [here](https://m.blog.naver.com/PostView.nhn?blogId=bsos1202&logNo=221090473029&proxyReferer=https%3A%2F%2Fwww.google.com%2F).

It is written in Korean.

# Source code
Written in Python 3.

```python
def solution(v):
    vx = [e[0] for e in v]
    vy = [e[1] for e in v]
    
    idx = list(set(v[0]+v[1]+v[2]))
    
    answer = [0, 0]
    for i in idx:
        if vx.count(i) == 1:
            answer[0] = i
        if vy.count(i) == 1:
            answer[1] = i

    return answer
```

If you use XOR operation, your code becomes shorter.
Cascaded XOR derives an unique value in 3 values.

```python
def solution(v):
    answer = []
    
    answer.append(v[0][0]^v[1][0]^v[2][0])
    answer.append(v[0][1]^v[1][1]^v[2][1])

    return answer
```

# What I learned
I learned how to use `list.count(value)` to count the number of value in a python list.

And `set()` operation does not allow the nested list e.g. `[[1,2],[2,1]]`. So I concatenated all of sub-lists and used `set()`.

# Future challenges
1. [ ] please write the solution once more. 
2. [ ] Debug it in my head.
3. [ ] Follow another solution. 

# Reference
[\[카카오 코딩테스트\]3. 직사각형 좌표 구하기](https://m.blog.naver.com/PostView.nhn?blogId=bsos1202&logNo=221090473029&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

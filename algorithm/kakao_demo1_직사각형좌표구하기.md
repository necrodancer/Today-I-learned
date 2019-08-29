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
    answer = [0, 0]
    
    keys = list(set(v[0]+v[1]+v[2]))
    
    vx = [arr[0] for arr in v]
    vy = [arr[1] for arr in v]
    
    for key in keys:
        if vx.count(key) == 1:
            answer[0] = key
        if vy.count(key) == 1:
            answer[1] = key
            
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

- [x] please write the solution once more. 
- [x] Debug it in my head.
- [x] Follow another solution. 

# Reference
[\[카카오 코딩테스트\]3. 직사각형 좌표 구하기](https://m.blog.naver.com/PostView.nhn?blogId=bsos1202&logNo=221090473029&proxyReferer=https%3A%2F%2Fwww.google.com%2F)

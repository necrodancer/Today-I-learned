# Flood filling algorithm for numpy array

```python
import numpy as np

def flood_fill(a,xx,yy,target=0,replace=1):
    stack = []
    if target == replace:
        return False
    if a[xx,yy] != target:
        return False
    stack.append([xx,yy])
    while len(stack) != 0:
        x, y = stack[-1]
        del stack[-1]
        w = y
        e = y

        while True:
            if w == a.shape[1]-1:
                break
            if a[x,w+1] == target and w < a.shape[1]-1:
                w = w + 1
            else:
                break
        while True:
            if a[x,e-1] == target and e-1 > 0:
                e = e - 1
            else:
                break

        for i in range(e,w+1):
            a[x,i] = replace
            if x-1 >= 0:
                if a[x-1,i] == target:
                    stack.append([x-1,i])
            if x+1 < a.shape[0]:
                if a[x+1,i] == target:
                    stack.append([x+1,i])
    return True

a = np.array([[1,1,1,0,0],
             [0,0,1,1,0],
             [0,1,1,0,1],
             [0,1,1,0,1],
             [0,1,0,0,1],
              [0,1,1,1,0]])
a = a*255
print(a)
print('\n')
count = 1
for i in range(0,a.shape[0]):
    for j in range(0, a.shape[1]):
        cond = flood_fill(a,i,j,target=255, replace= count)
        if cond == True:
            count = count + 1
print(a)
```

x=[11,22,33,44,55]

y=x

y[0]=1111

print(x)
print(y)

from copy import deepcopy
m=[1,2,3,4,5]
n=deepcopy(m)

n[0]=100

print(m)
print(n)
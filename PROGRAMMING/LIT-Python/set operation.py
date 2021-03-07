s=set([1,2,3,4,5])

s1=([4,5,6,7])

s.union(s1)

print(s)

print(s.difference(s1))    #here s in not updated

print(s)

s.difference_update(s1)    #here s is updated with the operation value
print(s)

s=set([1,2,3,4,5])

s1=([4,5,6,7])




list=[5,3,8,6,7,2,41,5,41,2,75,84,1,2,3,4,74,12,11,0,1,2,5,7,48]

for i in range(len(list)):
    for j in range(len(list)):
        if j < len(list)-1:
            k = j + 1
            if list[j] > list[k]:
                list[j], list[k] = list[k], list[j]


print(list)


"""
nums=[1,5,8,9,6,5,4,7]

for i in range(len(nums)):
    for j in range(i):
        if nums[j] > nums[i]:
            nums[j],nums[i]=nums[i],nums[j]

print(nums)


"""
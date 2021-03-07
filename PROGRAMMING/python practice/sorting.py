nums=[1,5,8,9,6,5,4,7]

for i in range(len(nums)):
    for j in range(i+1,len(nums)):

        if nums[j]> nums[i]:
            nums[i],nums[j] = nums[j],nums[i]

print(nums)
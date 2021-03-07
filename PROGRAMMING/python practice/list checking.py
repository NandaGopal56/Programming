'''
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count

'''

def sum13(nums):
    if len(nums)>=1:
        sum=0
        i=0
        while (i<=len(nums)-1):
            #print(i)
            if nums[i] != 13:
                print(nums[i])
                sum = sum+nums[i]
                i += 1
                
            else:
                print('nope')
                x = i+2
                if x <= len(nums):
                    i = i+2
                else:
                    i+=1
        return sum
    else:
        return 0

print(sum13([1,2,2,1]))
"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
"""


def sum67(nums):
    sum = 0
    flag =True
    for i in nums:
        if i != 6 and flag:
            sum  += i
        
        else:
            flag = False
        
        if i == 7:
            flag = True


    return sum


print(sum67([1, 2, 2, 6, 99, 99, 7]))
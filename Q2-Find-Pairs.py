#Write a prgram to find all pairs of integers whose sum is equal to a given number


'''
#Possible questions
1. Does array contain only positive numbers ?
2. What if the same pair repeats twice, should we print it two times
3. Do we need to print only distinct pairs ? does (3,3) is a valid pair given a sum of 6 ?(line no.14 & 15 is for this part)

'''
def FindPairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

Mylist = [1,2,3,2,3,4,5,6]
FindPairs(Mylist, target=6)
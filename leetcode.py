# two sum
# Given an array of integers, return indices of 
# the two numbers such that they add up to a specific target.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def two_sum(nums, target):

    if len(nums) <=1:
        return False

    difference = {}
    # iterating over the list of numbers
    for i in range(len(nums)):
        # if the number is in dictionary, return the position of the 
        #current number plus the difference's value at key = nums[i]
        if nums[i] in difference:
            return [difference[nums[i]], i]
        # if the number isn't in the dictionary, add it
        else:
            # dictionary key is the difference of target - num in nums
            # dictionary value is index of difference
            difference[target - nums[i]] = i

    return False

print two_sum([2,7,11,15], target = 9) == [0,1]
print two_sum([5,4,7,2,6], target = 10) == [1,4]
print two_sum([1], target = 8) == False


# palindrome number

# determine whether an integer is a palindrome, *(do this without extra space)*

def is_palindrome(i):

    





# add two numbers

# You are given two linked lists representing two non-negative numbers. The 
# digits are stored in reverse order and each of their nodes contain a single 
# digit. Add the two numbers and return it as a linked list.
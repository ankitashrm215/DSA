'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]
'''
def productExceptSelf(nums):

    
    ''' This is the brute force approach
    Time complexity: O(n*n) where n is the length of nums
    Space complexity: O(n) for allProd
    '''
    l = len(nums)
    allProd = []
    for i in range(0, l):
        j = 0
        prod = 1
        while j < l:
            if i != j:
                prod = prod * nums[j]
            j = j + 1
        allProd.append(prod)
    return allProd
print(productExceptSelf([1,2,4,6]))
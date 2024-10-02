'''
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
'''
def subarraySumEqualsK(nums, k):
    '''
    This is brute force approach where a subset of array is taken for each element
    Time Complexity: O(n*n) where n is length of array
    Space Complexity: O(1)
    '''
    l = len(nums)
    count = 0
    for i in range(0, l):
        if nums[i] == k:
            count += 1
        j = i + 1
        total = nums[i]
        while j < l:
            total = total + nums[j]
            if total == k:
                count += 1
            j = j + 1
    return count
print(subarraySumEqualsK([1,1,1], 2))
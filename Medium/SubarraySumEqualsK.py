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
    The drawback of this is for large values of n it gives "Time Limit Exceeded"
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

def slidingWindow(nums, k):
    '''
    This approach is applicable only when array has only positive numbers
    Time Complexity: O(n) where n is length of array
    Space Complexity: O(1)
    '''
    l = len(nums)
    if l == 0:
        return 0
    elif l == 1 and nums[0] == k:
        return 1
    
    start = 0
    end = 0
    total = nums[0]
    count = 0
    while start < l:
        if start > end:
            end = start
            total = nums[start]
        
        if total < k: # when total is less than target, expand window
            end += 1
            if end == l:
                break
            total+=nums[end]
        elif total > k: # when total is greater than target, decrease window
            total -= nums[start]
            start+=1
        else: # when total is equal to target, increase count
            count = count + 1
            total -= nums[start]
            start += 1
    return count

def subarraySumEqualsKOptimized(nums, k):

    '''
    The prefix sum approach is applicable when array has both positive and negative numbers
    Time Complexity: O(n) where n is length of array
    Space Complexity: O(n) for dictionary
    '''
    total = 0
    prefixDict = {}
    count = 0

    for i in range(0, len(nums)):
        total += nums[i]
        if total == k:
            count += 1
        if (total - k) in prefixDict:
            count += prefixDict[total - k]
        if total in prefixDict:
            prefixDict[total] += 1
        else:
            prefixDict[total] = 1
    return count

print(subarraySumEqualsK([1,1,1], 2))
print(slidingWindow([4, 2, 1, 6, 3, 1, 2], 12))
print(subarraySumEqualsKOptimized([1, -1, 1, 1, 1, 3], 3))
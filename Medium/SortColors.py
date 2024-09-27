'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
def sortColors(nums):

    '''
    Maps colors into a hash map
    Time complexity: O(n) where n is the length of nums
    Sppace complexity: O(n) where n is the length of nums
    '''
    colorsDict = {}
    for color in nums:
        if color in colorsDict:
            colorsDict[color].append(color)
        else:
            colorsDict[color] = [color]
        
    res = []
    if 0 in colorsDict:
        res.extend(colorsDict[0])
    if 1 in colorsDict:
        res.extend(colorsDict[1])
    if 2 in colorsDict:
        res.extend(colorsDict[2])
    nums[:] = res
    return nums


def sortColorsOptimized(nums):
    
    '''
    Implements quick sort partition
    Time complexity: O(n) where n is the length of nums
    Sppace complexity: O(1) for in-place sorting
    '''
    def swap(i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    i = 0
    l = 0
    length = len(nums)
    r = length - 1
    while i <= r:
        if nums[i] == 0:
            swap(i, l)
            l = l + 1
        elif nums[i] == 2:
            swap(i, r)
            r = r - 1
            i = i - 1
        i = i + 1
    return nums

print(sortColors([2,0,1]))
print(sortColorsOptimized([2,0,2,1,1,0]))
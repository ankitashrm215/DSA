'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].
'''

def longestConsecutiveSequence(nums):

        ''' This is the brute force approach that uses sorting
            Time complexity: O(nlogn) where n is the length of nums
            Space complexity: O(n) + O(n) for sorting list and tempList
        '''
        l = len(nums)
        if l == 1:
            return 1

        #sort list in O(nlogn)
        nums.sort()

        res = 1
        i = 0
        tempList=[]
        while i < l:
            j = i + 1            
            if(j < l and nums[j] - nums[i] == 1): #for consecutive sequence
                i = i + 1
                res = res + 1
            elif (j < l and nums[j] == nums[i]): #for duplicates
                i = i + 1
            else: #for non consecutve numbers
                i = j
                tempList.append(res)
                res = 1
        tempList.sort(reverse=True)
        return tempList[0] if len(tempList) > 0 else 0

def longestConsecutiveOptimized(nums):

        ''' This is otimized approach that uses set. Set uses hash set hence finding an item is set is O(1)
            Time complexity: O(n) where n is the length of nums
            Space complexity: O(1) for longest
        '''
        l = len(nums)
        numsSet = set(nums)
        if l == 1:
            return 1
        
        longest = 0
        for n in nums:
            if (n-1) not in numsSet: #check start of sequence
                l = 0
                while (n + l) in numsSet:
                    l = l + 1
                longest = max(l, longest)
        return longest

print(longestConsecutiveSequence([2,20,4,10,3,4,5]))
print(longestConsecutiveOptimized([2,20,4,10,3,4,5]))

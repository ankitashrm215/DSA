'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
Example 1:
Input: nums = [1,2,2,3,3,3], k = 2
Output: [2,3]

Example 2:
Input: nums = [7,7], k = 1
Output: [7]
'''

def topKFrequent(nums, k):

    ''' This is the brute force approach that uses dictionary and sorting to
    achieve the desired solution.
    Time complexity: O(n) + O(mlogn) + O(k.n) where n is the length of nums
    Space complexity: O(n)
    '''
    tempDict = {}
    #create dictionary with item as key and frequency as value
    for num in nums:
        if num in tempDict:
            tempDict[num] = tempDict[num] + 1
        else:
            tempDict[num] = 1
        
    #sort values of dict
    valuesList = list(tempDict.values())
    valuesList.sort(reverse=True)

    #fetch k most occurences
    topKVals = valuesList[0:k]
    res = []

    #fetch elements corresponding to most occurences
    for topVal in topKVals:
        for key,val in tempDict.items():
            if val == topVal and key not in res:
                res.append(key)
                break
    return res

print(topKFrequent([1,2,2,3,3,3], 2))

def topKFrequentOptimised(nums, k):

    ''' This is an optimised approach that uses bucket sort
    Time complexity: O(n) where n is the length of nums
    Space complexity: O(n)
    '''
    tempDict = {}

    #create dictionary with item as key and frequency as value
    for num in nums:
        if num in tempDict:
            tempDict[num] = tempDict[num] + 1
        else:
            tempDict[num] = 1
        
    arr = []
    for _ in range(0,len(nums)):
        arr.append([])

    #add item to array at frequency index
    for key,val in tempDict.items():
        arr[val-1].append(key)
        
    res = []

    #fetch top k lemenets from right of array
    for i in range(len(arr)-1, -1, -1):
        for item in arr[i]:
            res.append(item)
            if(len(res) == k):
                return res
    return res

print(topKFrequentOptimised([1,2,2,3,3,3], 2))
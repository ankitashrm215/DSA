'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
''' 

def groupAnagrams(strs):
    ''' 
    This function uses brute force approach where sorted strings are the keys of the dictionary 
    and all strings whose sorted values is equal to key are stored in values
    Time complexity: O(n) + O(nlogm) where n is number of elements in strs and m is average length of each string
    Space complexity: O(n)
    '''
    sortedDict = {}
    for s in strs:
        sortedStr = "".join(sorted(s))
        if(sortedStr in sortedDict):
            sortedDict[sortedStr].append(s)
        else:
            sortedDict[sortedStr] = [s]    
        return sortedDict.values()      
print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))

def groupAnagramsOptimized(strs):
    ''' 
    This function uses an optimised approach where frequency of each character of a string is stored as a key 
    and value is the list of strings
    Time complexity: O(n*m*c) where c is constant 26,
                     n is no. of elements in strs
                     m is average length of individual string
    Space complexity: O(1) + O(n) + O(n)
    '''
    dict1 = {}
    for word in strs:
        freqList = [0] * 26
        for char in word:
            freqList[ord(char) - ord('a')] += 1
        freqTuple = tuple(freqList)
        if(freqTuple in dict1.keys()):
            dict1[freqTuple].append(word)
        else:
            dict1[freqTuple] = [word]
    return dict1.values()
print(groupAnagramsOptimized(["act","pots","tops","cat","stop","hat"]))
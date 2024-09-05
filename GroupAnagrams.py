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

        sortedDict = {}
        for s in strs:
            sortedStr = "".join(sorted(s))
            if(sortedStr in sortedDict):
                sortedDict[sortedStr].append(s)
            else:
                sortedDict[sortedStr] = [s]
        return list(sortedDict.values())

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
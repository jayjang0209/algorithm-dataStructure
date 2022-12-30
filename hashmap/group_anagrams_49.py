"""
49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
https://leetcode.com/problems/group-anagrams/description/
"""

import collections


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    map = collections.defaultdict(list)
    for str in strs:
        map[''.join(sorted(str))].append(str)
    return list(map.values())


# s = ["eat","tea","tan","ate","nat","bat"]
# s = ["", ""]
s = ["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]
print(groupAnagrams(s))

"""
Complexity Analysis

Time Complexity: O(NKlog⁡K)O(NK \log K)O(NKlogK), where NNN is the length of strs, 
and KKK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N)O(N) 
as we iterate through each string. Then, we sort each string in O(Klog⁡K)O(K \log K)O(KlogK) time.

Space Complexity: O(NK)O(NK)O(NK), the total information content stored in ans.
"""
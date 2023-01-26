"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    tmp = strs[0]
    for i in range(1, len(strs)):
        while tmp != strs[i][:len(tmp)]:
            tmp = tmp[:len(tmp) - 1]
    return tmp
        
    
strs = ["c","acc","ccc"]
#Output: "fl"
print(longestCommonPrefix(strs))
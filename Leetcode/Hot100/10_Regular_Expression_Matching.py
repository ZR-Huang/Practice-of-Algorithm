'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLen, pLen = len(s), len(p)
        dp = [[False]*(pLen+1) for _ in range(sLen+1)]
        dp[0][0] = True
        for i in range(sLen+1):
            for j in range(1, pLen+1):
                if p[j-1] != '*':
                    if i > 0 and (s[i-1]==p[j-1] or p[j-1]=='.'):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    if j>=2:
                        dp[i][j] |= dp[i][j-2]
                    if i>=1 and j>=2 and (s[i-1]==p[j-2] or p[j-2]=='.'):
                        dp[i][j] |= dp[i-1][j]
        
        return dp[-1][-1]

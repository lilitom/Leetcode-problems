'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8



#------------------------------------------------------------------------------------
import collections
class Solution(object):
    def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [[0 for j in xrange(n)] for i in xrange(n)]

        for i in xrange(n - 1, -1, -1):
            dp[i][i] = 1
            for j in xrange(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]
    def longestPalindromeSubseq2(self, s):
        d = {}
        def f(s):
            if s not in d:
                maxL = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)

slu=Solution()
t=slu.longestPalindromeSubseq2('abca')
print t




#参考：

#相似题目
# https://leetcode.com/problems/longest-palindromic-subsequence/#/description
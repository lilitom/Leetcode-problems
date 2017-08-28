'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb".
'''
# coding=utf-8
# -*- coding:utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n - 1):
            P[i] = (R > i) and min(R - i, P[2 * C - i])  # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen) // 2: (centerIndex + maxLen) // 2]

    def longestPalindrome2(self, s):
        st = 0
        maxl = 0
        dp = [[False] * 1000 for i in range(1000)]
        for i in reversed(range(len(s))):
            for j in range(i, len(s)):
                if s[i] == s[j] and (i + 1 > j - 1 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > maxl:
                        st = i
                        maxl = j - i + 1

        return s[st:st + maxl]

    def longestPalindrome3(self, s): #中心向两边计算
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1;
            r += 1
        return s[l + 1:r]
    

slu_=Solution()
print(slu_.longestPalindrome3('abcddcba'))
#参考：https://leetcode.com/problems/longest-palindromic-substring/description/
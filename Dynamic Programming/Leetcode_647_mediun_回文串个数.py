'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
# -*- coding:utf-8 -*-
class Solution(object):
    def countSubstrings(self, s): #暴力破解
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res

    def countSubstrings2(self, s): #简化版的暴力
        return sum(s[i:j] == s[i:j][::-1] for j in range(len(s) + 1) for i in range(j))

    def countSubstrings3(self, s): #动态规划的思想，时间有点久
        cnt = 0  # count of pallindromes encountered
        if s:
            n = len(s)
            # a dynamic programming table, dp[i][j] = True if s[i:j+1] is pallindrome
            dp = [[True for j in range(n)] for i in range(n)]

            # each character is pallindrome, so dp[i][i] = True
            # also counting pallindromes of length 1
            for i in range(n):
                dp[i][i] = True
                cnt += 1

            for length in range(2, n + 1):  # length ranges from 2 to n
                for start in range(n):  # start index ranges from 0 to n-1
                    i = start
                    j = start + length - 1  # end index for a string of length "length" starting at index start
                    if 0 <= i < j < n:  # if indices are within string under consideration
                        dp[i][j] = False
                        if s[i] == s[j] and dp[i + 1][j - 1] == True:  # if s[i] == s[j] and s[i+1:j] is pallindrome
                            dp[i][j] = True
                            cnt += 1
        return cnt
slu_=Solution()
print(slu_.countSubstrings('abcddcba'))

#参考：https://leetcode.com/problems/palindromic-substrings/description/
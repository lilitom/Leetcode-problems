'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2 or n==3:
            return n-1
        res=1
        while n>4:
            res*=3
            n-=3
        return res*n
slu_=Solution()
print slu_.integerBreak(12)
#参考：https://leetcode.com/problems/integer-break/description/
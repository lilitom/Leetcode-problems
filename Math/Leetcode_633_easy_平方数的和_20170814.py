'''
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#我的方法 my way
#coding=utf-8
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(0,int(pow(c,0.5))+1):
            if int(pow(c-pow(i,2),0.5))==pow(c-pow(i,2),0.5):
                return True
        return False





#相关链接
#https://leetcode.com/problems/sum-of-square-numbers/description/

'''
Implement int sqrt(int x).

Compute and return the square root of x.


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#coding=utf-8
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans=x
        delata=0.001
        while ans*ans-x>delata:
            ans=(ans+x/ans)/2
        return ans




#œ‡πÿ¡¥Ω”
#https://leetcode.com/problems/sqrtx/description/
#http://www.guokr.com/question/461510/
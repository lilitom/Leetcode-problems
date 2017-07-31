'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class Solution(object):
    def isUgly(self, n):
        """
        :type num: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n==1:
            return True
        t2=0;t3=0;t5=0
        k=[0]*n
        k[0]=1
        for i in range(1,n):
            k[i]=min(k[t2]*2,min(k[t3]*3,k[t5]*5))
            if k[i]==k[t2]*2:
                t2=t2+1
            if k[i]==k[t3]*3:
                t3=t3+1
            if k[i]==k[t5]*5:
                t5=t5+1
        return k[n-1]
slu=Solution()
t=slu.isUgly(10)
print t







#参考：
#https://leetcode.com/problems/ugly-number-ii/discuss/



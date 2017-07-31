'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        t_temp=[0]*len(primes)
        k=[0]*n
        k[0]=1
        for i in range(1,n):
            min_tmp=k[t_temp[0]]*primes[0]
            for j in range(1,len(primes)):
                if k[t_temp[j]]*primes[j]<min_tmp:
                    min_tmp=k[t_temp[j]]*primes[j]
            k[i]=min_tmp
            for m in range(len(primes)):
                if k[i]==k[t_temp[m]]*primes[m]:
                    t_temp[m]=t_temp[m]+1
        return k[n-1]
slu=Solution()
t=slu.isUgly(12,[2,7,13,19])
print t








#参考：
#https://leetcode.com/problems/super-ugly-number/description/



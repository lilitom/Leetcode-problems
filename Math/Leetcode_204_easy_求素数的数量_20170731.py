'''
Description:

Count the number of prime numbers less than a non-negative number, n.


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#我的方法 my way
#coding=utf-8
#超时
class Solution(object):
    def isPrimes(self, nums):
        for i in range(2,nums / 2 + 1):
            if nums % i == 0:
                return False
        return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=[]
        for i in range(2,n):
            if self.isPrimes(i):
                count.append(i)
        return len(count)
slu_=Solution()
slu_.countPrimes(16)

#通过的方法
class Solution:
# @param {integer} n
# @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)
slu_=Solution()
print slu_.countPrimes(120)




#相关链接
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description
# http://blog.csdn.net/linhuanmars/article/details/23164149
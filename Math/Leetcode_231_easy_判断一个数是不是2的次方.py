'''
Given an integer, write a function to determine if it is a power of two.


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#我的方法 my way
#coding=utf-8
def isPowerOfTwo(i):#my way1
    while not i%2:
        i=i/2
        if i==1:
            return True
    return False

def isPowerOfThree(i): #my way2
    if i<=0:return False
    while i%2==0:
        i=i/2
    return i==1
print isPowerOfThree(2)

def isPowerOfTwo2(i):
    count=0
    while n>0:
        count+=n&1
        n>>=1
    return count==1

def isPowerOfTwo3(self, n):
    """
    :type n: int
    :rtype: bool
    """
    if n<=0:
        return False
    return not (n&(n-1));


#相关链接
#https://leetcode.com/problems/power-of-two/description/
'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#coding=utf-8
def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    i=1
    while num>0:
        num=num-i
        i=i+2
    return num==0
def isPerfectSquare2(num):
    """
    :type num: int
    :rtype: bool
    """
    x=num
    while x*x>num:
        x=(x+num/x)>>1
    return x*x==num

cc=isPerfectSquare2(16)
print cc




#œ‡πÿ¡¥Ω”
#https://leetcode.com/problems/valid-perfect-square/description/

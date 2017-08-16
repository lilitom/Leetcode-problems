'''
mplement pow(x, n).就是求一个数的多少次方的预算


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#coding=utf-8
def myPow(x, n):
    if n < 0:
        x = float(1) / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            pow *= x
        x *= x
        n >>= 1
    return pow
cc=myPow(4,16)
print cc


#相关链接
#https://leetcode.com/problems/powx-n/description/

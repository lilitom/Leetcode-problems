'''
GGiven two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#牛逼方法
class Solution(object):
    def multiply(self,num1, num2):
        product = [0] * (len(num1) + len(num2))
        pos = len(product) - 1

        for n1 in reversed(num2):
            tempPos = pos
            for n2 in reversed(num1):
                product[tempPos] += int(n1) * int(n2)
                product[tempPos - 1] += product[tempPos] / 10
                product[tempPos] %= 10
                tempPos -= 1 #注意这里
            pos -= 1 #注意这里

        pt = 0
        while pt < len(product) - 1 and product[pt] == 0:
            pt += 1

        return ''.join(map(str, product[pt:]))


slu=Solution()
t=slu.multiply('121','45')
print t


#参考：
#https://leetcode.com/problems/multiply-strings/#/description
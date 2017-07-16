'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

就是[1,9,9] 加1后为 [2,0,0]

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#牛逼方法
class Solution(object):
    def plusOne(self,digits):
        n=len(digits)
        for i in range(n-1,-1,-1):
            if digits[i]<9:
                digits[i]=digits[i]+1
                return digits
            digits[i]=0
            if i==0:
                digits.insert(0,1)
        return digits

slu=Solution()
t=slu.plusOne([9,9,9])
print t

#我的方法
class Solution(object):
    def pluseOne(self,digits):
        if not digits[len(digits)-1]==9:
            digits[len(digits) - 1]=digits[len(digits)-1]+1
            return digits
        later_flag=1
        for i in range(len(digits)-1,-1,-1):
            if later_flag==1:
                digits[i]=digits[i]+1
                if digits[i]==10:
                    digits[i]=0
                    if i==0:
                        digits.insert(0,1)
                    later_flag=1
                else:
                    later_flag=0
        return digits

slu=Solution()
t=slu.pluseOne([9,0,0])
print t




#参考：
#https://leetcode.com/problems/plus-one/#/description
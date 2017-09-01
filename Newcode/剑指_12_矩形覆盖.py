# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        n=number
        # write code here 
        if n==0:
            return 0
        start,a,b=0,0,1
        while start<n:
            a,b=b,a+b
            start=start+1
        return b
#https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6?tpId=13&tqId=11163&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking&tPage=1
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
'''
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent<0:
            base=float(1)/base
            exponent=-exponent
        pow=1
        while exponent:
            if exponent&1:
                pow*=base
            base*=base
            exponent>>=1
        return pow
#https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00?tpId=13&tqId=11165&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
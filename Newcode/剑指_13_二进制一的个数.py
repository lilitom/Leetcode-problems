# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
# -*- coding:utf-8 -*-
def rectCover(number):
    count=0
    while number:
        if number&1:
            count=count+1
        number=number>>1
    return count
	
def rectCover2(number):	
	count=0
    while number:
        count=count+1
		number=(number-1)&number
    return count
##https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8?tpId=13&tqId=11164&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
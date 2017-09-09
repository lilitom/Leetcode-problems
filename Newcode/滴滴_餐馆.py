'''
题目描述

某餐馆有n张桌子，每张桌子有一个参数：a可容纳的最大人数；有m批客人，每批客人有两个参数：b人数、c预计消费金额。在不允许拼桌的情况下，请实现一个算法选择其中一部分客人，使得总预计消费金额最大。

输入描述

输入包括m+2行。
第一行包括2个整数n(1<=n<=50000)，m(1<=m<=50000);
第二行为n个参数a，即每个桌子可容纳的最大人数，以空格分隔，范围均在32位int范围内;
接下来m行，每行两个参数b和c，分别表示第i批客人的人数和预计消费金额，以空格分隔，范围均在32位int范围内。
输出描述

输出一个整数，表示最大的总预计消费金额。
输入例子

3 5
2 4 2
1 3
3 5
3 7
5 9
1 10
输出例子

20
'''

import sys
import bisect
n,m=map(int,sys.stdin.readline().strip().split())
desk_size=map(int,sys.stdin.readline().strip().split())
desk_size.sort()
customer=[]
for i in range(m):
    customer.append(map(int,sys.stdin.readline().strip().split()))
customer.sort(key=lambda x:x[1],reverse=True)
max_count=0
for i in customer:
    pos=bisect.bisect_left(desk_size,i[0])
    if 0<=pos<len(desk_size):
        max_count+=i[1]
        del desk_size[pos]
print max_count
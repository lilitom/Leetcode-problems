# -*- coding:utf-8 -*-
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        n = n + 1
    return b
print fab(5)
print tt
#参考：https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-rankingn-ranking
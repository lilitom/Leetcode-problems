# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
输入一个链表，输出该链表中倒数第k个结
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        pre=head
        leng=0
        while head:
            head=head.next
            leng+=1
        if k>leng:
            return None
        for i in range(leng-k):
            pre=pre.next
        return pre
#https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a?tpId=13&tqId=11167&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
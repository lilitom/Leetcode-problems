# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
'''
输入一个链表，反转链表后，输出链表的所有元
'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        node=None
        while pHead:
            nxt=pHead.next
            pHead.next=node
            node=pHead
            pHead=nxt
        return node

#https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca?tpId=13&tqId=11168&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking
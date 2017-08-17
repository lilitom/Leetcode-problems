'''
Reverse a singly linked list.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#!/usr/bin/python
# -*- coding: UTF-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node=None
        while head:
            nxt=head.next
            head.next=node
            node=head
            head=nxt
        return node

L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(3)
L4=ListNode(3)
L5=ListNode(2)
L6=ListNode(1)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=L6
slu_=Solution()
print slu_.reverseList(L1)

#https://leetcode.com/problems/reverse-linked-list/description/
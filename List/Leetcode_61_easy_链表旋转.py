'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
链表的旋转  简单的旋转
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
#正确
# -*- coding:gb2312 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        fast = head
        while fast.next:
            fast = fast.next
        fast.next = head
        slow = head
        for i in range(k):
            slow = slow.next
        new_head = slow.next
        slow.next = None
        return new_head

        

#参考
#https://leetcode.com/problems/rotate-list/description/

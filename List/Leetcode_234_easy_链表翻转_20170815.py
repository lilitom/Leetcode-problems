'''
Given a singly linked list, determine if it is a palindrome.
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow: #链表的反转
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node:  # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True


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
print slu_.isPalindrome(L1)

#https://leetcode.com/problems/palindrome-linked-list/description/
#https://discuss.leetcode.com/topic/18952/python-easy-to-understand-solution-with-comments-operate-nodes-directly
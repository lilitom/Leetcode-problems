'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
#ÕýÈ·
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c1, c2 = '', ''
        while l1:
            c1 += str(l1.val)
            l1 = l1.next
        while l2:
            c2 += str(l2.val)
            l2 = l2.next
        c1=c1[::-1]
        c2=c2[::-1]
        num = str(int(c1) + int(c2))[::-1]
        dummy = ListNode(0)
        c = dummy
        for i in range(len(num)):
            c.next = ListNode(num[i])
            c = c.next
        return dummy.next
        


#²Î¿¼
#https://leetcode.com/problems/add-two-numbers/description/
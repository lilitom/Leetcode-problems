'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7


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
        c1, c2 = '', ''
        while l1:
            c1 += str(l1.val)
            l1 = l1.next
        while l2:
            c2 += str(l2.val)
            l2 = l2.next
        num = str(int(c1) + int(c2))
        dummy = ListNode(0)
        c = dummy
        for i in range(len(num)):
            c.next = ListNode(num[i])
            c = c.next
        return dummy.next
        
        
#my way 
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        node=None
        while head:
            nxt=head.next
            head.next=node
            node=head
            head=nxt
        return node

L1_7=ListNode(7)
L1_2=ListNode(2)
L1_4=ListNode(4)
L1_3=ListNode(3)

L2_5=ListNode(5)
L2_6=ListNode(6)
L2_4=ListNode(4)

L1_7.next=L1_2
L1_2.next=L1_4
L1_4.next=L1_3

L2_5.next=L2_6
L2_6.next=L2_4

slu_=Solution()
newl1=slu_.reverseList(L1_7)
newl2=slu_.reverseList(L2_5)

head1=newl1
head2=newl2

dummNode=ListNode(0)
dummNode.next=None
slow=dummNode
jingwei=0
while head1 or head2:
    if head1!=None and head2!=None:
        sum_val=head1.val+head2.val+jingwei
        head1=head1.next
        head2=head2.next
    elif head1!=None and head2==None:
        sum_val=head1.val+jingwei
        head1=head1.next
    else:
        sum_val=head2.val+jingwei
        head2=head2.next
    jingwei=0
    if sum_val>=10:
        sum_val=sum_val%10
        jingwei=1
    slow.next=ListNode(sum_val)
    slow=slow.next
dummNode=dummNode.next


#²Î¿¼
#https://leetcode.com/problems/add-two-numbers-ii/description/
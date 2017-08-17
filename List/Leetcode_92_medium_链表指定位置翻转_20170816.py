'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next=head
        pre=dummyNode

        for i in range(m-1):
            pre=pre.next
        start=pre.next
        then=start.next

        for i in range(n-m):
            start.next= then.next
            then.next=pre.next
            pre.next=then
            then=start.next
        print '1111'

    def reverseBetween2(self, head, m, n): #∫√¿ÌΩ‚
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next

        # reverse the [m, n] nodes
        reverse = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next

        pre.next.next = cur
        pre.next = reverse

        return dummyNode.next

L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(3)
L4=ListNode(4)
L5=ListNode(5)
L6=ListNode(6)
L7=ListNode(7)
L8=ListNode(8)
L9=ListNode(9)
L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=L6
L6.next=L7
L7.next=L8
L8.next=L9

slu_=Solution()
print slu_.reverseBetween2(L1,4,7)



#https://leetcode.com/problems/reverse-linked-list-ii/description/
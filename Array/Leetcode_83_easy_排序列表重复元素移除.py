'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
#正确
# -*- coding:gb2312 -*-
# -*- coding:gb2312 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):#some problems
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummNode=ListNode(0)
        dummNode.next=head
        jilu=set([])
        slow=dummNode
        while slow is not None and slow.next is not None:
            jilu.add(slow.val)
            if slow.next.val in jilu:
                slow.next=slow.next.next
            slow=slow.next
        return dummNode.next
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next     # skip duplicated node
            cur = cur.next     # not duplicate of current node, move to next node
        return head
list1=ListNode(1)
list2=ListNode(1)
list3=ListNode(2)
list4=ListNode(3)
list5=ListNode(3)
list1.next=list2
list2.next=list3
list3.next=list4
list4.next=list5

slu_=Solution()
slu_.deleteDuplicates(list1)

#参考
#https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/








        


#参考
#https://leetcode.com/problems/add-two-numbers/description/
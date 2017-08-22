'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.

'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNodeA
        """
        dummNode = ListNode(0)
        dummNode.next = head

        slow = dummNode
        while slow!=None and slow.next!=None:
            if slow.next.val==val:
                slow.next = slow.next.next
            else:
                slow=slow.next
        return dummNode.next
L1=ListNode(1)
L2=ListNode(2)
L3=ListNode(6)
L4=ListNode(3)
L5=ListNode(4)
L6=ListNode(5)
L7=ListNode(6)

L1.next=L2
L2.next=L3
L3.next=L4
L4.next=L5
L5.next=L6
L6.next=L7


slu_=Solution()
print slu_.removeElements(L1,6)
      

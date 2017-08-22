'''
Given a linked list, determine if it has a cycle in it.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow=head
            fast=head.next
            while slow is not fast:
                slow=slow.next
                fast=fast.next.next
            return True
        except:
            return False
	def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
		slow=fast=head
        while fast and fast.next:  # 注意这里的fast 和 fast.next的顺序不能写反
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False


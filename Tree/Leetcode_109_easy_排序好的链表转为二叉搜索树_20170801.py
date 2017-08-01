'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#coding=utf-8
# coding=utf-8
# 我的方法
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:return None
        mid=int(len(nums)//2)
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        count = []
        while head:
            count.append(head.val)
            head = head.next
        return self.sortedArrayToBST(count)

Listlist=ListNode(1)
Listlist.next=ListNode(2)
Listlist.next.next=ListNode(3)
Listlist.next.next.next=ListNode(4)
Listlist.next.next.next.next=ListNode(5)
Listlist.next.next.next.next.next=ListNode(6)
Listlist.next.next.next.next.next.next=ListNode(7)
slu_ = Solution()
t = slu_.sortedListToBST(Listlist)
print t



#大牛做法
#使用前后快慢指针移动以确定中间的位置，然后再将链表切分
#使用递归
def sortedListToBST2(self, head):
    if not head:
        return
    if not head.next:
        return TreeNode(head.val)
    # here we get the middle point,
    # even case, like '1234', slow points to '2',
    # '3' is root, '12' belongs to left, '4' is right
    # odd case, like '12345', slow points to '2', '12'
    # belongs to left, '3' is root, '45' belongs to right
    slow, fast = head, head.next.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # tmp points to root
    tmp = slow.next
    # cut down the left child
    slow.next = None
    root = TreeNode(tmp.val)
    root.left = self.sortedListToBST2(head)
    root.right = self.sortedListToBST2(tmp.next)
    return root





#参考：
#https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
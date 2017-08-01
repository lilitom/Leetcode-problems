'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#coding=utf-8
# coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:return None
        mid=int(len(nums)//2)
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root


slu_ = Solution()
t = slu_.sortedArrayToBST([1,2,3£¬4,5,6,7,8,9,10,11,12,13,14,15])
print t





#²Î¿¼£º
#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
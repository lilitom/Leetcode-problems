'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0
        leftheight=self.maxDepth(root.left)
        rightheight=self.maxDepth(root.right)
        return 1+max(leftheight,rightheight)

input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18


slu_ = Solution()
print input_all
t = slu_.maxDepth(input_all)
print t




#²Î¿¼£º
#https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description
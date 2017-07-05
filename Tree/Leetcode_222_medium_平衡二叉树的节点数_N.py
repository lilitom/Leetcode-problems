'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
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


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)



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
t = slu_.countNodes(input_all)
print t



#²Î¿¼£º
#https://leetcode.com/problems/count-complete-tree-nodes/#/description
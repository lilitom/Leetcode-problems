'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
input_18.left=TreeNode(11)
input_18.right=TreeNode(199)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18

input_7=TreeNode(7)
input_11=TreeNode(11)
input_9 = TreeNode(9)
input_9.right=input_11
input_12 = TreeNode(12)
input_all2 = TreeNode(6)
input_all2.left = input_9
input_all2.right = input_12


slu_ = Solution()
print input_all
t = slu_.invertTree(input_all)
print t



#采用栈的方法
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
input_18.left=TreeNode(11)
input_18.right=TreeNode(199)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18

input_7=TreeNode(7)
input_11=TreeNode(11)
input_9 = TreeNode(9)
input_9.right=input_11
input_12 = TreeNode(12)
input_all2 = TreeNode(6)
input_all2.left = input_9
input_all2.right = input_12


slu_ = Solution()
print input_all
t = slu_.invertTree(input_all)
print t



#参考：
#https://leetcode.com/problems/invert-binary-tree/#/description
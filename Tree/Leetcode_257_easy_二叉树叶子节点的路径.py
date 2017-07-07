'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#coding=utf-8
import Queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BinTreePath(self,root):#求得任意到叶子节点的路径
        if not root:
            return []
        res,stack=[],[(root,'')]
        while stack:
            Node, ls =stack.pop()
            if not Node.left and not Node.right:
                res.append(ls+str(Node.val))
            if Node.left:
                stack.append((Node.left,ls+str(Node.val)+'->'))
            if Node.right:
                stack.append((Node.right,ls+str(Node.val)+'->'))
        return res   

input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
input_18.right = TreeNode(199)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18

slu_ = Solution()
t=slu_.BinTreePath(input_all)
print t





#参考：
#https://leetcode.com/problems/binary-tree-paths/#/description
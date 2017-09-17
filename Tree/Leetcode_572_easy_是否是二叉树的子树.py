'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
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
    def isMatch(self,s,t):
        if not(s and t):
            return s is t
        return (s.val==t.val and self.isMatch(s.left,t.left) and self.isMatch(s.right,t.right))
    def issubtree(self,s,t):
        if self.isMatch(s,t):
            return True
        if not s:
            return False
        return self.issubtree(s.left,t) or self.issubtree(s.right,t)
input_3=TreeNode(3)
input_3.left=TreeNode(4)
input_3.left.left=TreeNode(1)
input_3.left.right=TreeNode(2)
input_3.right=TreeNode(5)


input_4=TreeNode(4)
input_4.left=TreeNode(1)
input_4.right=TreeNode(2)


slu_=Solution()
print slu_.issubtree(input_3,input_4)



#²Î¿¼£º
#https://leetcode.com/problems/subtree-of-another-tree/description/
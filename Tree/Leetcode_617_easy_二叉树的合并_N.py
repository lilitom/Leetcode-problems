'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
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
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2: return None
        ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return ans
    def mergeTrees2(self, t1, t2):#这种递归方式比较好理解一些
        
        if not t1 and not t2:
            return None
        
        elif t1 and not t2:
            return t1
        
        elif t2 and not t1:
            return t2
        
        r = TreeNode(t1.val + t2.val)
        r.left = self.mergeTrees(t1.left, t2.left)
        r.right = self.mergeTrees(t1.right, t2.right)
        return r

input_3=TreeNode(3)
input_4=TreeNode(4)
input_5 = TreeNode(5)
input_5.left=input_3
input_5.right=input_4
input_18 = TreeNode(18)
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
t = slu_.mergeTrees(input_all,input_all2)
print t




#参考：
#https://leetcode.com/problems/merge-two-binary-trees/#/description
'''
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
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
    def averageOfLevels(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([0, 0])
                info[depth][0] += node.val
                info[depth][1] += 1
                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        dfs(root)

        return [s/float(c) for s, c in info]

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
t = slu_.averageOfLevels(input_all)
print t




#²Î¿¼£º
#https://leetcode.com/problems/merge-two-binary-trees/#/description
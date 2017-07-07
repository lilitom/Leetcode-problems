'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root): #得到最小路径方法1
        if root == None:
            return 0
        if root.left == None or root.right == None:
            return self.minDepth(root.left) + self.minDepth(root.right) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1

    def minDepth2(self, root): #得到最小路径方法2
        if not root: return 0
        d = map(self.minDepth2, (root.left, root.right))
        return 1 + (min(d) or max(d))

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
t = slu_.minDepth(input_all)
print t

#-----------------------------------------------------------
#我的方法
#coding=utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth3(self, root): #得到最小路径方法3
        if not root: return 0
        queue=Queue.Queue()
        queue.put(root)
        num_cout=0
        while queue:
            num_cout=num_cout+1
            for j in range(queue.qsize()):
                root=queue.get()
                if root.right:
                    queue.put(root.right)
                if root.left:
                    queue.put(root.left)
                if  not root.left and not root.right:
                    return num_cout


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
t = slu_.minDepth(input_all)
print t





#参考：
#https://leetcode.com/problems/minimum-depth-of-binary-tree/#/description
'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
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
    def lowestCommonAncestor(self, root, p, q):#递归
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if not root or root == p or root == q:
                return root
            if self.isnode(p, q):
                return p
            if self.isnode(q, p):
                return q
            if self.isnode(root.left, p) and self.isnode(root.left, q):
                root = root.left
            if self.isnode(root.right, p) and self.isnode(root.right, q):
                root = root.right
            else:
                return root

    def isnode(self, mother, child):
        if mother:
            if mother == child:
                return True
            else:
                return self.isnode(mother.left, child) or self.isnode(mother.right, child)
        return False


    def lowestCommonAncestor2(self, root, p, q): #通过使用栈来进行 
        stack = [root]
        parent = {root: None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:
            q = parent[q]
        return q

input_3 = TreeNode(3)
input_4 = TreeNode(4)
input_5 = TreeNode(5)
input_5.left = input_3
input_5.right = input_4
input_18 = TreeNode(18)
input_18.left = TreeNode(11)
input_18.right = TreeNode(199)
input_all = TreeNode(2)
input_all.left = input_5
input_all.right = input_18

slu_=Solution()
c=slu_.lowestCommonAncestor2(input_all,input_4,input_18)
print c.val






#参考：
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
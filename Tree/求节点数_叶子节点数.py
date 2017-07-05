class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def leave(self,root):#总的节点数
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return (self.leave(root.left)+self.leave(root.right)+1)
    def min_leave(self,root): #叶子节点数
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return (self.leave(root.left)+self.leave(root.right)+1)



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
print input_all
t = slu_.leave(input_all)
print t
#coding=utf-8
import Queue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}


    def getWidth(self,root): #求树的宽度
        curwidth = 1
        maxwidth = 0
        q = Queue.Queue()
        q.put(root)
        while not q.empty():
            n = curwidth
            for i in range(n):
                tmp = q.get()
                curwidth -= 1
                if tmp.left:
                    q.put(tmp.left)
                    curwidth += 1
                if tmp.right:
                    q.put(tmp.right)
                    curwidth += 1
            if curwidth > maxwidth:
                maxwidth = curwidth
        return maxwidth
    def getheight(self,root): #求二叉树的高度
        if not root:
            return 0
        left_height=self.getheight(root.left)
        right_height=self.getheight(root.right)
        return 1+max(left_height,right_height)


    def DepTraval(self, root): #深度遍历
        if not root:
            return None
        stack=[root]
        while stack:
            Node=stack.pop()
            print Node.val
            if  Node.right:
                stack.append(Node.right)
            if  Node.left:
                stack.append(Node.left)


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


    def BroTraval(self,root):#广度遍历(层次遍历)
        if not root:
            return None
        queue=Queue.Queue()
        queue.put(root)
        while queue:
            Node=queue.get()
            print Node.val
            if  Node.left:
                queue.put(Node.left)
            if  Node.right:
                queue.put(Node.right)


    def FindLeave(self,root): #叶子节点的值
        if not root:
            return None
        stack = [root]
        leavevalue=[]
        while stack:
            root = stack.pop()
            if not root.right and not root.left:
                leavevalue.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return leavevalue


    def sumofLeftLeaves(self,root): #求得左叶子节点的和
        if not root:
            return 0
        stack=[root]
        res=0
        while stack:
            Node=stack.pop()
            if Node.left:
                stack.append(Node.left)
                if not Node.left.left and not Node.left.right:#注意这里的表达
                    res+=Node.left.val
                if Node.right:
                    stack.append(Node.right)
        return res

    def sumofLeaves(self,root): #求叶子节点之和
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        left_sum=self.sumofLeaves(root.left)
        right_sum=self.sumofLeaves(root.right)
        return left_sum+right_sum

    def sumofallnode(self,root): #返回所有节点之和
        ans=[]
        def pre_ordef(root):
            if not root:
                return
            pre_ordef(root.left)
            ans.append(root.val)
            pre_ordef(root.right)
        pre_ordef(root)
        return sum(ans)

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
t=slu_.sumofallnode(input_all)
print t

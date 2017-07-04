'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) == 0:
            return 0
        local_op = 0
        global_op = 0
        for i in range(1, len(prices)):
            local_op = max(prices[i] - prices[i-1] + local_op, prices[i] - prices[i-1])#注意这里不要写错
            global_op = max(global_op, local_op)
        return global_op


Su_=Solution()
print Su_.maxProfit([7, 1, 5, 3, 6, 4])


#解释：
# 动态规划问题
这道题求进行一次交易能得到的最大利润。如果用brute force的解法就是对每组交易都看一下利润，取其中最大的，总用有n*(n-1)/2个可能交易，所以复杂度是O(n^2)。
很容易感觉出来这是动态规划的题目，其实跟Maximum Subarray非常类似，用“局部最优和全局最优解法”。思路是维护两个变量，一个是到目前为止最好的交易，另一个
是在当前一天卖出的最佳交易（也就是局部最优）。递推式是local[i+1]=max(local[i]+prices[i+1]-price[i],0), global[i+1]=max(local[i+1],global[i])。
这样一次扫描就可以得到结果，时间复杂度是O(n)。而空间只需要两个变量，即O(1)。 




#参考：
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/#/solutions
#http://blog.csdn.net/linhuanmars/article/details/23162793




#相似题目
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description
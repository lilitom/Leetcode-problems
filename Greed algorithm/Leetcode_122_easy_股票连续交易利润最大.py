'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


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
        self.ans=[]
        if prices==None or len(prices)==0:
            return 0
        for i in range(1,len(prices)):
            self.ans.append(max(0,prices[i]-prices[i-1]))
        return sum(self.ans)
Su_=Solution()
print Su_.maxProfit([7, 1, 5, 3, 6, 4])



#相关链接
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/#/description
# http://blog.csdn.net/linhuanmars/article/details/23164149
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


'''


'''
根据上述的求最大的可以把数组分成两分然后求解比较最大的即可
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8





#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class Solution(object):
    def subMaxProfit(self,subprice):
        if subprice==None or len(subprice)==0:
            return 0
        local_op=0
        global_op=0
        for i in range(1,len(subprice)):
            local_op=max(local_op+subprice[i]-subprice[i-1],max(0,subprice[i]-subprice[i-1]))
            global_op=max(local_op,global_op)
        return global_op
    def maxProfit(self,prices):
        if prices==None or len(prices)==0:
            return
        self.pre_max=[]
        self.post_max=[]
        for k in range(1,len(prices)-1):
            self.pre_max.append(self.subMaxProfit(prices[0:k+1]))
            self.post_max.append(self.subMaxProfit(prices[k:len(prices)]))
        max_profit=[x+y for x,y in zip(self.pre_max,self.post_max)]
        return max(max_profit)
Su_=Solution()
print Su_.maxProfit([7, 19, 5, 3, 6, 4])




#参考：
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/#/description
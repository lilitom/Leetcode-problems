'''
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8



#------------------------------------------------------------------------------------
class Solution(object):
    def findTargetSumWays(self, nums, S):
        count = {0: 1}
        for x in nums:
            count2 = {}
            for tmpSum in count:
                count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
                count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
            count = count2
        return count.get(S, 0)

    def findTargetSumWays2(self, nums, S):
        from collections import defaultdict
        memo = {0: 1}
        for x in nums:
            m = defaultdict(int)
            for s, n in memo.iteritems():
                m[s + x] += n
                m[s - x] += n
            memo = m
        return memo[S]
    def findTargetSumWays3(self,nums,S):
        def backtrack(nums,S,start):
            if start==len(nums):
                if S==0:
                    return 1
                return 0
            return backtrack(nums,S-nums[start],start+1)+backtrack(nums,S+nums[start],start+1)
        return backtrack(nums,S,0)


slu=Solution()
t=slu.findTargetSumWays2([1, 1 ,1,1,1],3)
print t




#²Î¿¼£º
#https://leetcode.com/problems/target-sum/#/description
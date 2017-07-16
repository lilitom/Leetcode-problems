'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#高级方法
#采用异或的方法
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing=0
        for i in range(len(nums)):
            missing^=(i+1)^nums[i]
        return missing		
slu=Solution()
t=slu.missingNumber([0,1,2,3,4,6])
printt




#------------------------------------------------------------------------------------
#coding=utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        return n*(n+1)/2-sum(nums)
slu=Solution()
t=slu.missingNumber([0,1,2,3,4,6])
printt



#参考：
#https://leetcode.com/problems/missing-number/#/description
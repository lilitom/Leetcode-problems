'''
iven an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
Credits:

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]
            

			
			
			
			
#·½°¸
nums=[1,4,3,2,3,5]
low=0
high=len(nums)-1
while high>low:
    mid=int((high+low)/2)
    count=0
    for i in range(len(nums)):
        if nums[i]<=mid:
            count=count+1
    if count>mid:
        high=mid
    else:
        low=mid+1
print(low)
#²Î¿¼
#https://leetcode.com/problems/find-the-duplicate-number/description/


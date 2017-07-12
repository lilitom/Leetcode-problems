'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(nums[i])
                nums.append(0)
        return nums
slu=Solution()
t=slu.moveZeroes([0,1,0,3,12])
print t





#²Î¿¼£º
#https://leetcode.com/problems/move-zeroes/#/description
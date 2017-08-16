'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
nums=[1,1,2,2,3,3,4,4,5,6,6,7,7,8,8,9,9] 
输出5
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
nums=[1,1,2,2,3,3,4,4,5,6,6,7,7,8,8,9,9]
for i in range(len(nums)):
    a = nums.pop(0)
    if len(set(nums)) == len(nums) / 2:
        print(a)
    nums.append(a)


#方案AC
nums=[1,1,2,2,3,3,4,4,5,6,6,7,7,8,8,9,9]
result=0
for i in range(len(nums)):
    result^=nums[i]
print(result
#参考
#https://leetcode.com/problems/single-number/description/


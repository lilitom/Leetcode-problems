'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
nums=[1,2,2,4]
count = [0] * (len(nums) + 1)
for x in nums:
    count[x] += 1
for x in range(1,len(count)):
    if count[x]==2:
        twice=x
    if count[x]==0:
        never=x
print(twice,never)

#²Î¿¼
#https://leetcode.com/problems/set-mismatch/description/

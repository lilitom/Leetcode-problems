'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ? n/2 ? times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in range(len(nums)):
            dict[str(nums[i])] = dict.get(str(nums[i]), 0) + 1
        aa=sorted(dict.items(), key=lambda aa: aa[1], reverse=True)
        if aa[0][1]>len(nums)/2:
            return int(aa[0][0])


slu=Solution()
t=slu.majorityElement([1,1,1,2,3,3,4,5])
print t




#²Î¿¼£º
#https://leetcode.com/problems/majority-element/#/description
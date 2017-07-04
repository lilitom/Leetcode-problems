'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#from https://leetcode.com/problems/range-sum-query-immutable/#/description
#------------------------------------------------------------------------------------
#标准方法--牛 the best way-niu
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num, #巧妙的地方就在这里

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
NumArray_=NumArray([-2, 0, 3, -5, 2, -1])
print NumArray_.sumRange(0,-2)



#------------------------------------------------------------------------------------
#我的方法 my way
#coding=utf-8
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.accu = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            self.accu[i]=self.accu[i-1]+nums[i-1]
        print self.accu

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int 
        :type j: int
        :rtype: int 
        """
        return self.accu[j + 1] - self.accu[i]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
NumArray_=NumArray([-2, 0, 3, -5, 2, -1])
print NumArray_.sumRange(0,-2)

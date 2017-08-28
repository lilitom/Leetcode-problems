'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row,cols=len(matrix),len(matrix[0])
        low,high=0,row*cols-1
        while low<=high:             #注意这里要有等号的
            mid=(low+high)/2
            num=matrix[mid/cols][mid%cols]
            if num==target:
                return True
            if num<target:
                low=mid+1
            else:
                high=mid-1
        return False






#参考：
#https://leetcode.com/problems/search-a-2d-matrix/description/
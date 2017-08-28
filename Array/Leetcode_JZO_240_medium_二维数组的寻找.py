'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.



'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
class Solution(object):
    def searchMatrix(self, matrix, target):
        if  matrix==[[]]:
            return False
        if  matrix==[]:
            return False
        if target<min(min(matrix)) or target>max(max(matrix)):
            return False
        row,col=0,len(matrix[0])-1
        rows=len(matrix)
        while row<rows and col>=0:
            if matrix[row][col]==target:
                return True
                break
            elif matrix[row][col]>target:
                col=col-1
            else:
                row=row+1
        return False
		
slu_=Solution()
matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
slu_.searchMatrix(matrix,17)






#²Î¿¼£º
#https://leetcode.com/problems/search-a-2d-matrix-ii/description/
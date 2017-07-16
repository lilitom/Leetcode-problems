'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.

'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous=nums[len(nums)-1]
            for j in range(len(nums)):
                temp=nums[j]
                nums[j]=previous
                previous=temp
        return nums
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a=[0]*len(nums)
        for i in range(len(nums)):
            a[(i+k)%len(nums)]=nums[i]
        for i in range(len(nums)):
            nums[i]=a[i]
        return nums

    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a=nums
        for i in range(k):
            a.insert(0,a.pop())
        for i in range(len(nums)):
            nums[i] = a[i]
        return nums


slu=Solution()
t=slu.rotate3([1,2,3,4,5,6,7],3)
print t



#²Î¿¼£º
#https://leetcode.com/problems/rotate-array/#/description
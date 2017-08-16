'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
nums=[1,1,2,2,3,4,5,5]
res=[0,0]
diff=0
for i in nums:
    diff^=i
diff&=(-diff)
for j in nums:
    if j&diff ==0:
        res[0]^=j
    else:
        res[1]^=j
print(res)
#²Î¿¼
#https://leetcode.com/problems/single-number-iii/description/
#http://blog.csdn.net/yeruby/article/details/49853385
#http://www.cnblogs.com/aboutblank/p/4741051.html


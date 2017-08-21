'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.



'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------
#正确
# -*- coding:gb2312 -*-
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        pos1 = {v: pos for pos, v in enumerate(list1)}
        length = len(list2) + len(list1)
        result = []
        mind = length
        for i, v in enumerate(list2):
            j = pos1.get(v, length)
            if i + j < mind:
                result = [v]
                mind = i + j
            elif i + j == mind:
                result.append(v)
        return result
list1=["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2=["KFC", "Shogun", "Burger King"]
slu_=Solution()
slu_.findRestaurant(list1,list2)

#参考
#https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/








        


#参考
#https://leetcode.com/problems/add-two-numbers/description/
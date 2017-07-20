'''
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''

#解释 比如[1 2 3 4 5] 要求和为6 无论第一个人怎么取 他总是输 因为他取的第一个数 第二个人总可以得到一个加起来超过6
#South China University of Technology  
#Author:Guohao
#coding=utf-8



#------------------------------------------------------------------------------------
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
            """
            :type maxChoosableInteger: int
            :type desiredTotal: int
            :rtype: bool
            """
            if (1 + maxChoosableInteger) * maxChoosableInteger/2 < desiredTotal:
                return False
            self.memo = {}
            return self.helper(range(1, maxChoosableInteger + 1), desiredTotal)


    def helper(self, nums, desiredTotal):

        hash = str(nums)
        if hash in self.memo:
            return self.memo[hash]

        if nums[-1] >= desiredTotal:
            return True

        for i in range(len(nums)):
            if not self.helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                self.memo[hash]= True
                return True
        self.memo[hash] = False
        return False
slu_=Solution()
print slu_.canIWin(5,10)





#参考：https://leetcode.com/problems/can-i-win/#/description


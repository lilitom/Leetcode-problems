# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number==1:
            return 1
        elif number==2:
            return 2
        else:
            dp=[0]*(number+1)
            dp[1]=1
            dp[2]=2
            for i in range(3,number+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[number]
#参考：https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=%2Fta%2Fcoding-interviews&qru=%2Fta%2Fcoding-interviews%2Fquestion-ranking%2Fquestion-rankingn-ranking
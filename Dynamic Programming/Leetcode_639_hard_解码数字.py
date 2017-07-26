'''
A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
简单来说就是一个解码的过程，*可以选择0-9之间的数字
'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#方法一
s='12**610'
n=len(s)
if n==0:
    print 0
if s[0]==0:
    print 0
dp=[0]*(len(s)+1)
dp[0]=1
if s[0]=="*":
    dp[1]=9
else:
    dp[1]=1
mod = 1000000007
for i in range(1,n):
    one=0
    if s[i]=="*":
        one=9
    elif s[i]=='0':
        one=0
    else:
        one=1
    # dp[i+1]=(dp[i]%mod*one)%mod
    last=s[i-1]
    if last!='*' and last>'2' or last=='0':
        continue
    cur=s[i]
    two=0
    if cur!='*' and last!='*':
        if last=='2' and cur>'6':
            two=0
        else:
            two=1
    elif cur!='*':
        if cur>'6':
            two=1
        else:
            two=2
    elif last!='*':
        if last=='1':
            two=9
        else:
            two=6
    else:
        two=15
    dp[i+1]=(dp[i]%mod*one+dp[i-1]%mod*two)%mod
print dp[n]


#方法二 查表的方式
'''
We know the DP, let dp[i] is the total ways of decoding for ith position of a string,function is dp[i]=digit1 * dp[i-1]+digit2 * dp[i-2],where digit1 is the ways of only 1 digit at the its position, digit2 is the ways of the decoding of only 2 digits at pos i and i-1,for the digit1, it is clear and simple: "*"->9, "0"->0, "1"-"9"->1, for the digit2, there are some combinations, to simply this, use a table to look up.

                 S[i]   "*"  "0"  "1"-"6"  "7"-"9"
         s[i-1]     |---------------------------------
          "*"       |   15    2      2        1     
          "1"       |   9     1      1        1       
          "2"       |   6     1      1        0     
        "0","3"-"9" |   0     0      0        0    
'''
def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        table2=[[15,2,2,1],[9,1,1,1],[6,1,1,0]]
        table2Colmap={"*":0,"0":1,"1":2,"2":2,"3":2,"4":2,"5":2,"6":2,"7":3,"8":3,"9":3}

        def get_1digit_ways(si):
		#这里查找的是当前的位置，如果是*那么有9个数字，如果是0则为0，如果是介于两者之间的话则有1个取值
            if si=="0": ans=0
            else:
                ans=9 if si=="*" else 1
            return ans

        def get_2digit_ways(table2,table2Colmap,si_1,si):
		#这里就是需要查表得，就是two的位置
            ans=0
            if si_1=="0" or "3"<=si_1<="9":
                ans=0
            else:
                i=0 if si_1=="*" else  ord(si_1)-ord("0")
                j=table2Colmap[si]
                ans=table2[i][j]
            return ans

        n = len(s)
        mod=1000000007
        if n==0 or s[0]=="0": return 0

        dp1=get_1digit_ways(s[0])
        if n==1: return dp1
        dp2_digt1ways=get_1digit_ways(s[1])
        dp2_digt2ways=get_2digit_ways(table2,table2Colmap,s[0],s[1])

        dp2=dp1*dp2_digt1ways+dp2_digt2ways
        if n==2: return dp2
        for i in xrange(2,n):
            digit1=get_1digit_ways(s[i])
            digit2=get_2digit_ways(table2,table2Colmap,s[i-1],s[i])

            dp=(dp2*digit1%mod + dp1*digit2%mod)%mod
            dp2,dp1=dp,dp2
        return dp
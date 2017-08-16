'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.


'''
#South China University of Technology  
#Author:Guohao
#coding=utf-8
#------------------------------------------------------------------------------------

#coding=utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x<10:
            return True
        b=x
        d=-1
        while x:
            x/=10
            d+=1
        print d
        left=pow(10,d)
        right=10
        for i in range(d/2+1):
            l1=b/left
            r2=b%10
            if l1!=r2:
                return False
            b=(b%left)/10
            left=left/100
        return True
        
#方法2
if x<0:
    print False
p=x
q=0
while p>=10:
    q*=10
    q+=p%10
    p/=10
print q==x/10
print p==x%10

#相关链接
#https://leetcode.com/problems/palindrome-number/description/
#http://www.cnblogs.com/fanyabo/p/4183006.html

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return 0
        if length == 1:
            return rotateArray[0]
        left, right = 0, length - 1

        while left <= right:
            mid = (left + right) >> 1
            if rotateArray[mid] > rotateArray[right]:
                left = mid+1
            elif rotateArray[mid] < rotateArray[right]:
                right = mid
            else:
                right -= 1
            if left >= right:
                break
        return rotateArray[left]
slu_=Solution()
tt=slu_.minNumberInRotateArray([8,9,1,2,3,4,5,6,7])
print tt
#参考：https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
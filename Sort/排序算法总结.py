#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time
import sys
sys.setrecursionlimit(1500) # set the maximum depth as 1500
lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
print '排序前',nums



#冒泡排序--交换排序----------------------------------------------
def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                nums[i],nums[j]=nums[j],nums[i]
    return nums


    
    
#插入排序---------------------------------------------------------
def insert_sort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0:
            if nums[j]>key:
                nums[j+1],nums[j]=nums[j],nums[j+1]
            j-=1
    return nums



    
#希尔排序--插入排序----------------------------------------------
def shell_sort(lists):
    count = len(lists)
    step = 3                                  #这里的设置反比于运行时间
    group = int(count/step)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group=group/step
    return lists


    
    
#快速排序-交换排序--------------------------------------------
def parttion(v, left, right):
    key = v[left]
    low = left
    high = right
    while low < high:
        while (low < high) and (v[high] >= key): #注意这里是while
            high -= 1
        v[low],v[high] = v[high],v[low]
        while (low < high) and (v[low] <= key): #注意这里是while 还有<=
            low += 1
        v[low], v[high] = v[high], v[low]
    return low
def quicksort(v, left, right):
    if left < right:
        p = parttion(v, left, right)
        quicksort(v, left, p-1)
        quicksort(v, p+1, right)
    return v


    
#选择排序-简单选择排序-------------------------------------------
def select_sort(nums):
    for i in range(len(nums)):
        min_po=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[min_po]:
                min_po=j
        nums[min_po],nums[i]=nums[i],nums[min_po]
    return nums

    
#归并排序--------------------------------------------------------
def merge(left,right):
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:             #这里的是j 记得<=
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result += left[i:]                  #注意这里的是在while的下面 不是被包含的哈
    result += right[j:]
    return result
def merge_sort(nums):
    if len(nums)==1:
        return nums
    middle_parttion=len(nums)/2
    left=merge_sort(nums[:middle_parttion])
    right=merge_sort(nums[middle_parttion:])
    return merge(left,right)


#基数排序
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists    
    
#测试----------------------------------------------------------------------
lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
print bubble_sort(nums)
b=time.time()
print '冒泡： ',b-a,'s'


lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
print insert_sort(nums)
b=time.time()
print '插入： ',b-a,'s'


lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
shell_sort(nums)
b=time.time()
print '希尔： ',b-a,'s'


lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
print quicksort(nums,0,len(nums)-1)
b=time.time()
print '快排： ',b-a,'s'


lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
print select_sort(nums)
b=time.time()
print '选择： ',b-a,'s'



lists_befor=[x for x in xrange(10)]
nums=random.sample(lists_befor, 10)
a=time.time()
print merge_sort(nums)
b=time.time()
print '归并： ',b-a,'s'




















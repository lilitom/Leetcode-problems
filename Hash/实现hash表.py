# -*- coding:utf-8 -*-
def find(arr,j):
    len1=len(arr)
    hasharr=[0]*(len1+5)
    arr2=[0]*(len1+5)
    i=0
    while i<len1:
        a=arr[i]%17
        while arr2[a]!=0:
            a=a+1
            if i==len1:
                i=0
        hasharr[a]=arr[i]
        arr2[a]=1
        i+=1
    print hasharr
    print '\n'
    print arr2

    num=j%17
    while num<len1+5:
        if arr2[num]==1:
            if hasharr[num]==j:
                print 'Find the element',num
                num=len1+5
            else:
                num+=1
        else:
            print 'The element is no exist'
            num=len1+5
arr=[10,8,15,45,7,5,6,2,11,23,4,778,9,5,12]
find(arr,45)
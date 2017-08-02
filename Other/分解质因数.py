import math
def Getchildren(nums):
    for i in range(2,nums/2):
        if nums%i==0:
            print i
            print '*'
            return Getchildren(nums/i)
Getchildren(90)

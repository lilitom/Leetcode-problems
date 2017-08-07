def isPowerOfThree(i):
    if i<=0:return False
    while i%4==0:
        i=i/4
    return i==1
print isPowerOfThree(64)
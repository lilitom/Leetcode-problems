#ÏêÏ¸²Î¿¼ http://blog.csdn.net/littlethunder/article/details/25637173
# coding=utf-8
def lcs(a,b):
    c=[[0 for i in range(100)] for j in range(100)]
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i-1][j],c[i][j-1])
    print c[len(a)][len(b)]

max_lcs('BDCABA','ABCBDAB')
lcs('BDCABA','ABCBDAB')
#ÏêÏ¸²Î¿¼ http://blog.csdn.net/baidu_28312631/article/details/47418773
# coding=utf-8
input_data=[7,3,8,8,1,0,2,7,4,4,4,5,2,6,5]
data_matrix=[[0 for i in range(5)] for j in range(5)]
dp_matrix=[[0 for i in range(5)] for j in range(5)]
t=0
for i in range(5):
    for j in range(i+1):
        data_matrix[i][j]=input_data[t]
        t+=1
for i in range(5):
    dp_matrix[4][i]=data_matrix[4][i]
for i in range(3,-1,-1):
    for j in range(0,i+1):
        dp_matrix[i][j]=max(dp_matrix[i+1][j],dp_matrix[i+1][j+1])+data_matrix[i][j]
print dp_matrix[0][0]

'''
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
'''
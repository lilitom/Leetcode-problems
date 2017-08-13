'''
小易老师是非常严厉的,它会要求所有学生在进入教室前都排成一列,并且他要求学生按照身高不递减的顺序排列。有一次,n个学生在列队的时候,小易老师正好去卫生间了。学生们终于有机会反击了,于是学生们决定来一次疯狂的队列,他们定义一个队列的疯狂值为每对相邻排列学生身高差的绝对值总和。由于按照身高顺序排列的队列的疯狂值是最小的,他们当然决定按照疯狂值最大的顺序来进行列队。现在给出n个学生的身高,请计算出这些学生列队的最大可能的疯狂值。小易老师回来一定会气得半死。 
输入描述:

输入包括两行,第一行一个整数n(1 ≤ n ≤ 50),表示学生的人数
第二行为n个整数h[i](1 ≤ h[i] ≤ 1000),表示每个学生的身高


输出描述:

输出一个整数,表示n个学生列队可以获得的最大的疯狂值。

如样例所示: 
当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。
示例1
输入

5
5 10 25 40 25
输出

100
'''
n=raw_input()
nums=[int(x) for x in raw_input().split(' ')]
nums.sort()
result=[]
result.append(nums[-1])
nums.pop()
while len(nums):
    result.append(nums[0])
    result.insert(0,nums[1])
    result.append(nums[-1])
    result.insert(0,nums[-2])
    nums.pop()
    nums.pop()
    nums.pop(0)
    nums.pop(0)
    if len(nums)<4:
        break
if len(nums)==3:
    result.append(nums[0])
    result.append(nums[2])
    result.insert(0,nums[1])
elif len(nums)==2:
    if abs(result[0]-nums[0])+abs(result[-1]-nums[-1])>abs(result[0]-nums[-1])+abs(result[-1]-nums[0]):
        result.append(nums[-1])
        result.insert(0,nums[0])
    elif abs(result[0]-nums[0])+abs(result[-1]-nums[-1])==abs(result[0]-nums[-1])+abs(result[-1]-nums[0]):
        result.append(nums[0])
        result.append(nums[1])
    else:
        result.append(nums[0])
        result.insert(0,nums[1])
elif len(nums)==1:
    if abs(result[-1]-nums[0])>abs(result[0]-nums[0]):
        result.append(nums[0])
    else:
        result.insert(0,nums[0])
t=0
for i in range(len(result)-1):
    t=t+abs(result[i+1]-result[i])
print t
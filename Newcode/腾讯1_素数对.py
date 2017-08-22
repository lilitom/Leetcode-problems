'''
给定一个正整数，编写程序计算有多少对质数的和等于输入的这个正整数，并输出结果。输入值小于1000。
如，输入为10, 程序应该输出结果为2。（共有两对质数的和为10,分别为(5,5),(3,7)） 
输入包括一个整数n,(3 ≤ n < 1000)
'''
input_=int(raw_input())
nums = [x for x in range(1, input_)]
zhishu = []
for num in nums:
    if num > 1:
        for i in range(2, num/2):
            if (num % i) == 0:
                break
        else:
            zhishu.append(num)

cout_=0
for i in zhishu:
    if 2*i==input_:
        cout_=cout_+1
    if (input_-i) in zhishu:
        cout_=cout_+0.5
print int(cout_)
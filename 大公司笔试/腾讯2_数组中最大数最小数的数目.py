'''
有n个数，两两组成二元组，差最小的有多少对呢？差最大呢？
'''
while True:
    try:
        n=int(raw_input())
        input_data=sorted([int(x) for x in raw_input().split()])
        chazhi=[input_data[i+1]-input_data[i] for i in range(0,len(input_data)-1)]
        count=0
        min_count=0
        for i in range(len(chazhi)):
            if input_data[i+1]==input_data[i]:
                count=count+1
            else:
                min_count+=count*(count+1)/2
                count=0
        min_count+=count*(count+1)/2
        if  chazhi.count(0)==0:
            print chazhi.count(min(chazhi)),input_data.count(input_data[0])*input_data.count(input_data[-1])
        else:
            print min_count,input_data.count(input_data[-1])*input_data.count(input_data[0])
    except:
        break




#问题描述
# Description 
# 　　烽火台又称烽燧，是重要的军事防御设施，一般建在险要或交通要道上。一旦有敌情发生，白天燃烧柴草，通过浓烟表达信息；夜晚燃烧干柴，以火光传递军情，在某两座城市之间有n个烽火台，每个烽火台发出信号都有一定代价。为了使情报准确地传递，在连续m个烽火台中至少要有一个发出信号。请计算总共最少花费多少代价，才能使敌军来袭之时，情报能在这两座城市之间准确传递。 
# Input 
# 　　第一行：两个整数N，M。其中N表示烽火台的个数，M表示在连续m个烽火台中至少要有一个发出信号。接下来N行，每行一个数Wi，表示第i个烽火台发出信号所需代价。 
# Output 
# 　　一行，表示答案。 
# Sample Input 
# 5 3 
# 1 
# 2 
# 5 
# 6 
# 2

# Sample Output 
# 4

# Data Constraint 
# 对于50%的数据，M≤N≤1,000 。 对于100%的数据，M≤N≤ 100,000，Wi≤100。

可以参考
https://blog.csdn.net/A1847225889/article/details/77777009
https://blog.csdn.net/INCINCIBLE/article/details/51104886
其中这道题的动态规划的状态转移方程是比较简单的也就是
f[i]=min(f[j])+w[i] (max(0,i-m)<=j<i)
其中f[i]表示如果当前位置的火把被点燃时的最小代价，
最终要求得的则是f[i]中的i从n-m+1到n这段值中的最小值，

	for (int i = 1; i <= n; i++)
	{
		for (j = max(0, i - m); j<i; ++j)//分两段写的原因是为了卡常——你也可以并在一起，然后j的初值为max(0,i-m)
			f[i] = min(f[i], f[j]);
		f[i] += w[i];
	}


	int ans = 0x7f7f7f7f;
	for (i = n - m + 1; i <= n; ++i)
		ans = min(ans, f[i]);
	printf("%d\n", ans);
    
    

当然这样的速度是不行的，需要做相应的优化策略才可以，怎么个快法呢，在这样一类问题中可以使用叫做单调队列的做法
来实现。什么是单调队列呢？
先看->https://blog.csdn.net/zhelong3205/article/details/77624699
再看->https://www.youtube.com/watch?v=ShbRCjvB_yQ
最后看->https://blog.csdn.net/q547550831/article/details/51620320

是在看不懂可以看我的博客 https://www.jianshu.com/p/ceb8d62d6c4e

代码如下：
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int n, m;
int w[10];
int que[10], head = 0, tail = 0;
int f[10];
int main()
{
    scanf("%d%d", &n, &m);
    int i, j;
    for (i = 1; i <= n; ++i)
        scanf("%d", &w[i]);
    memset(f, 127, sizeof f);
    f[0] = 0;
    que[0] = 0;
    for (i = 1; i <= n; ++i)
    {
        if (que[head]<i - m)
            ++head;//将超出范围的队头删掉
        f[i] = f[que[head]] + w[i];//转移（用队头）
        while (head <= tail && w[que[tail]]>w[i])
            --tail;//将不比它优的全部删掉
        que[++tail] = i;//将它加进队尾
    }
    int ans = 0x7f7f7f7f;
    for (i = n - m + 1; i <= n; ++i)
        ans = min(ans, f[i]);
    printf("%d\n", ans);
}






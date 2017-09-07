'''
有一组单词，请编写一个程序，在数组中找出由数组中字符串组成的最长的串A，即A是由其它单词组成的(可重复)最长的单词。
给定一个string数组str，同时给定数组的大小n。请返回最长单词的长度，保证题意所述的最长单词存在。
测试样例：
["a","b","c","ab","bc","abc"],6
返回：3
'''

class LongestString:
    def getLongest(self, s, n):
        s.sort(key=len)
        for i in reversed(range(n)):
             if self.cotains(s[:i],s[i]):
                 return len(s[i])
    def cotains(self,str1,str2):
        q=[str2]
        while q:
            current=q.pop()
            if current=='':
                return True
            else:
                for i in str1:
                    if current.startswith(i):
                        q.append(current[len(i):])
        return False
#https://www.nowcoder.com/profile/4558295/codeBookDetail?submissionId=11158501
class Solution(object):
    def findAnagrams(self, s, p):

        list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dic={}
        flag=0
        l=len(p)
        final=[]
        if len(s)<len(p) or len(s)==0 or len(p)==0:
            return final

        for i in range(len(list1)):
            dic[list1[i]] = list[i]
        #print(dic)
        sum_p=1
        for i in range(l):
            sum_p*=dic[p[i]]
        #print(sum_p)
        sum_s=1
        while(flag<=len(s)-l):
            #print(flag)
            sum_s=1

            for i in range(l):
                sum_s*=dic[s[flag+i]]
            #print(sum_s)
            if sum_s==sum_p:
                final.append(flag)

            flag+=1
        return final
a=Solution()
s="absdasdaa"
p='asd'
print(a.findAnagrams(s,p))

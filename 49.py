class Solution(object):
    def groupAnagrams(self, strs):
        list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dic={}
        final=[]
        final1=[]
        if strs==['']:
            list=[]
            list.append(strs)
            return list
        elif len(strs)==1:
            return strs
        try:
            for i in range(len(list1)):
                dic[list1[i]]=list[i]
            for j in range(len(strs)):
                sum = 1
                for k in range(len(strs[j])):
                    sum*=dic[strs[j][k]]
                final.append(sum)
            #print(final)
            dicstr={}
            for q in range(len(strs)):
                dicstr[strs[q]]=final[q]
            #print(dicstr)
            dics = sorted(dicstr.items(), key=lambda obj: obj[1])
            final.sort()
            #print(dics)
            #print(final)
            for z in range(len(final)):
                if final[z-1]!=final[z]:
                    final1.append(final[z])
            #print(final1)
            final3=[[] for i in range(len(final1))]
            k=0
            final3[k].append(dics[0][0])
            #print(final3)

            for l in range(len(final)-1):
                if final[l]!=final[l+1]:
                    k += 1
                    final3[k].append(dics[l+1][0])
                    #print(final[l])
                else:
                    final3[k].append(dics[l+1][0])
            #print(final3)
            return final3
        except:
            list3=[]
            list3.append(strs)
            return list3
s=Solution()
list=["",""]

print(s.groupAnagrams(list))

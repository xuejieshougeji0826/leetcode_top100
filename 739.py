class Solution:
    def dailyTemperatures(self, T):
        l=len(T)
        nums=[]
        if l==0:
            return nums
        else:
            for i in range(l-1):
                for j in range(l-i-1):
                    if T[i+j+1]-T[i]>0:
                        nums.append(j+1)
                        break
                    else:
                        if j==l-i-2:
                            nums.append(0)
                        else:pass

            nums.append(0)
            return nums




r = Solution()
list1= [89,62,70,58,47,47,46,76,100,70]
print(r.dailyTemperatures(list1))

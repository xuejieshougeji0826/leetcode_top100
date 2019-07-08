class Solution:
    def flipAndInvertImage(self, Lists):

        l=len(Lists[0])
        for i in range(0,len(Lists)):
            Lists[i]=list(reversed(Lists[i]))
            print(Lists)
            for j in range(l):
                #List[i][j]=List[i][j]^1
                #print(Lists[i])
                if Lists[i][j]==0:
                    Lists[i][j] =1
                else :  Lists[i][j] =0
        return Lists


r=Solution()
list1=[[1,1,0],[1,0,1],[0,0,1]]
print(r.flipAndInvertImage(list1))
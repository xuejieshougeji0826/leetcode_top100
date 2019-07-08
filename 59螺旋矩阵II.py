class Solution:
    def generateMatrix(self, n):
        k=1
        j=0
        list= [[0]*n for i in range(n)]
        while (j<n):
            for a in range(j,n-j-1):
                list[j][a]=k
                k+=1
            for b in range(j,n-j-1):
                list[b][n-j-1]=k
                k+=1
            for c in range(n-j-1,j-1,-1):
                list[n-j-1][c]=k
                k+=1
                #print(list)
            for d in range(n-j-2,j,-1):
                list[d][j]=k
                k+=1
            #print(list)
            j+=1
        return list

s = Solution()
n=1
print(s.generateMatrix(n))

class Solution:
    def rotate(self, matrix):
        l=len(list[0])
        k=l
        p=0
        m=0
        while(k!=1):
            for i in range(p):
                matrix[p][p],matrix[p][l-p]=matrix[p][l-p],matrix[p][p]
            k-=1
        print(matrix)

s = Solution()
list  =[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
print(s.rotate(list))

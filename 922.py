class Solution:
    def sortArrayByParityII(self, A):
        l=len(A)
        i=0
        j=1
        while(j<l-1 and i<l-1):
                if A[i]%2==0:
                    if A[j]%2==1:
                        #swap(A[i],A[j])
                        j+=2
                        i+=2
                    else:

                        i+= 2
                else :
                    if A[j]%2==1:

                        i+=2
                    else:
                        print(A)
                        temp=A[i]
                        A[i]=A[j]
                        A[j]=temp
                        print(A)
                        i+=2
                        j+=2
            # except:
        if A[-2]%2==1:
            temp = A[-2]
            A[-2] = A[-1]
            A[-1] = temp
            return A
        else:return A

r = Solution()
list1=[3,1,2,4]
print(r.sortArrayByParityII(list1))


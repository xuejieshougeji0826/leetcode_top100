# str_n=[]
# # str="a b c d"
# # str_n2=[]
# # def reversed(str):
# #     str_n=str.split(' ')
# #     n=len(str_n)
# #     print(n)
# #     str1=''
# #     for num in range(int(n/2)):
# #         str_n2.append(str_n[num])
# #         #print(str_n2)
# #         #a=str_n.pop(0)
# #         str_n.append(str_n2[-1])
# #         str_n2.pop()
# #         #print('a',a)
# #     for num in range(int(n/2)):
# #         str_n.pop(0)
# #         #print(str_n2.pop())
# #     print("sss",str_n)
# #     for word in str_n:
# #         print('word:',word)
# #         str1+=word
# #     return str1
# # print(reversed(str))

n=2
fm=0
fz=0
for i in range(1,n+1):
    fm+=n*(n+1)
    fz+=2*n+1
    print(fm,fz)
print(fm,fz)
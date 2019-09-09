n=int(input())
def change(n):
    list=[]
    if n<=1:
        return 1
    for i in range(1,n+1):
        list.append(i)
    point=0
    time=0
    print(list)
    while (point!=list[-1]):
        l=len(list)
        point+=5
        if point>l:
            point-=l
        list.remove(list[point])
        time+=1
    return
print(change(n))
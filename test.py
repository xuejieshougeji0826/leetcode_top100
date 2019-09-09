def asd(numwords,words,numQuesiton,question):
    words.sort()
    words.reverse()
    result=[]
    print(words)
    for i in range(numQuesiton):
        if question[i]==1:
            result.append(words[0])
        if question[i] == 2:
            result.append(words[-1])
        if question[i]==3:
            result.append(words[-2])
        if question[i]==4:
            result.append(words[1])
        if question[i]==5:
            k=words[-1]
            k=k[::-1]
            result.append(k)
            words[-1]=k
            words.sort()
            words.reverse()

    return result

a = ["ah","cb","ef","gd"]
b=[1,2,3,4,5,1,2,3,4]
print(asd(3,a,len(b),b))
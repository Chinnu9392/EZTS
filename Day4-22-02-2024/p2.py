t=int(input())
for k in range(t):
    a="."
    s=input()
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        if d[i]>=2:
            print(i)
            break
        else:
            print(".")
        

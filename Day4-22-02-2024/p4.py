n=int(input())
d={}
for i in range(n):
    s=input()
    if s in d:
        d[s]+=1
    else:
        d[s]=1
m=max(d.values())
r=[i for i in d if d[i]==m] 
print(max(r),m)

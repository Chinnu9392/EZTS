#Find All Duplicate Elements in Array
n=int(input())
l=list(map(int,input().split()))[:n]
d=[]
for i in range(n):
    if l.count(l[i])>1:
        if l[i] in d:
            continue
        else:
            d.append(l[i])

for i in d:
    print(i)

#Find All Unique Elements in Array
n=int(input())
l=list(map(int,input().split()))[:n]
for i in l:
    if l.count(i)==1:
        print(i,end=" ")

t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cost=0
    for j in range(n):
        if a[j] >= x:
            cost= cost+ b[j]
    print(cost)

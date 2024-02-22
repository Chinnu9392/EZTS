t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for j in range(r):
        st,co=map(int,input().split())
        if co in d:
            d[co].append(st)
        else:
            d[co]=[st]
    for k in d:
        if len(d[k])>n and len(set(d[k])==len(d[k]):
            print(f"Scenario #{i+1} : Impossible")
            break
    else:
        print(f"Scenario #{i+1} : Possible")

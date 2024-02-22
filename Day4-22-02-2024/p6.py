# find the paths for a given node in a directed graph
"""
t=int(input())
dic={}
for i in range(t):
    s,d=input().split()
    if s not in dic:
        dic[s]=[d]
    else:
        dic[s].append(d)
f=input()
if f in dic:
    print(*dic[f],sep=" ")
else:
    print("None")
"""
# find the shortest paths for a given node in a directed and weighted graph
#approach 1
t=int(input())
dic={}
for i in range(t):
    s,d,distance=map(str,input().split())
    if s not in dic:
        dic[s]=[[distance,d]]
    else:
        dic[s].append([distance,d])
f=input()
if f in dic:
    dic[f].sort()
    print(f"{f}->{dic[f][0][1]}")
else:
    print("None")

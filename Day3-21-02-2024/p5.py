#even perfect numbers in a given range
#approach 1
'''
s,e=map(int,input().split())
r=[]
for i in range(s,e+1):
    f=[]
    for j in range(1,i):
        if i%j==0:
            f.append(j)
    if sum(f)==i and i%2==0:
        r.append(i)
print(r)'''
#approach 2
n=int(input())
s=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0
 

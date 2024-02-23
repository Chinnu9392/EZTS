s=input()
n=len(s)
r=""
c=1
for i in range(1,n):
    if s[i]==s[i-1]:
       c+=1
    else:
        r=r+s[i-1]+str(c)
        c=1
r=r+s[n-1]+str(c)
print(r)
        

#panagram
#approach 1
'''
s=input()
def pan(s):
    s.lower()
    a={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    for i in a:
        if i not in s:
            return "not panagram"
    else:
        return "panagram"
print(pan(s))'''
#approach 2
'''
s=input()
a=set(s)
if len(a)==27:
    print("yes")
else:
    print("No")'''
#approach 3
'''
s=input()
d={}
for i in s:
    if i not in d and i!=" ":
        d[i]=1
if len(d)==26:
    print("yes")
else:
    print("No")'''
        
#approach 4
'''
a={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
s=input()
d={}
for i in s:
    if i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
if len(d.keys())==26:
    print("yes")
else:
    print("No")'''












 

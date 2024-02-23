#occurenece of a character in a string
#approach 1
'''
s=input()
ch=input()
c=0
for i in s:
    if i==ch:
        c+=1
print(c)
'''
#approach 2
'''
s=input()
ch=input()
print(s.count(ch))
'''
#occurenece of a character in a string at even index
s=input()
ch=input()
c=0
for i in range(len(s)):
    if i%2==0 and s[i]==ch:
        c+=1
print(c)

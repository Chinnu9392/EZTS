#vowels in a string
#approach 1
"""
s=input()
v="aeiouAEIOU"
for i in s:
    if i not in v:
        print("No")
        break
else:
    print("Yes")
 """
#approach 2
'''
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i in v:
        c+=1
if c==len(s):
    print("Yes")
else:
    print("No")
    '''
#approach 3
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i not in v:
        c+=1
if c==0:
    print("Yes")
else:
    print("No")

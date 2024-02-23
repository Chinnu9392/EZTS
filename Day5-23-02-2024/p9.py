#count of words,vowels and consonants in a string
#approach 1
'''
t=int(input())
vowel="aeiou"
con="zxcvbnmlkjhgfdsqwrtyp"
for i in range(t):
    s=input().strip()
    s=s.lower()
    v=0
    c=0
    for j in s:
        if j in vowel:
            v+=1
        elif j in con:
            c+=1
    print(len(s.split(" ")),v,c)
'''
#approach 2
t=int(input())
vowel="aeiou"
for i in range(t):
    s=input().split()
    v=0
    c=0
    for j in s:
        for k in j:
            if k.isalpha():
                if k in vowel:
                    v+=1
                else:
                    c+=1
    print(len(s),v,c)
#approach 3
t=int(input())
vowel="aeiou"
for i in range(t):
    s=input().lower()
    v=0
    c=0
    for j in s:
        if k.isalpha():
            if k in vowel:
                v+=1
            else:
                c+=1
    print(len(s.split(" ")),v,c)    

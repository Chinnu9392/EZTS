#count of vowels and consonants in a string
#approach 1
'''
s=input()
v="aeiouAEIOU"
consonants="zxcvbnmlkjhgfdsqwrtypZXCVBNMLKJHGFDSQWRTYP"
vowel=0
con=0
for i in s:
    if i in v:
        vowel+=1
    elif i in consonants:
        con+=1
print(vowel,con)'''
#approach 2
s=input()
v="aeiouAEIOU"
vowel=0
con=0
for i in s:
    if i.isalpha():
        if i in v:
            vowel+=1
        else:
            con+=1
print(vowel,con)

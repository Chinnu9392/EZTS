#string methods
print("hello".endswith('o'))
print("hello".startswith('o'))
print("hello".replace('o','e'))
print("100".isdigit()) #checks each digit
print("hello".isalpha())
print("72".isdecimal()) #checks entire digit
print("72ab".isalnum())
print("Hello World".istitle())
print("Hello".upper())
print("Hello".lower())
print("Hello".swapcase())#converts upper into lower and vice versa
print("Hello world".title()) # converts every starting character of every word into uppercase
print("Hello".capitalize()) # convetrs the first character of a sting in upppercase
print("python cython".find("th")) #2
print("python cython".rfind("th")) #9
print("python cython".count("th")) #2

#string functions
print(len("Hello"))
print(max("Hello"))
print(min("Hello"))

# pass by reference
def myfun(x):
    x[0]=22
lst=[10,20,30,40]
myfun(lst)
print(lst)

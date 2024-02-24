def f1(self, x,y):
    return min(x,y)
class C:
    f=f1
    def g(self):
        print("Hello World")
ob=C()
print(ob.f(10,20))
ob.g()

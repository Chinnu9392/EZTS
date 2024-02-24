#ispalindrome

class check:
    def __init__(self,n):
        self.n = n
    def ispalindrome(self):
        if self.n == self.n[::-1]:
            print("Yes")
        else:
            print("No")
ob1 = check("Hello")
ob2 = check("sas")
ob1.ispalindrome()
ob2.ispalindrome()

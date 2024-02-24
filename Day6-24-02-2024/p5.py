class P:
    def __init__(self):
        print("hi")
class C(P):
    def __init__(self):
        super().__init__()
        print("hello")
ob=C()

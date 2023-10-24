class A:

    def __init__(self):
        print("from class A")

class B(A):

    def __init__(self):
        print('from class B')
        A.__init__(self)

class C(B):
    def __init__(self):
        print('from class c')
        B.__init__(self)


object_c = C()
from itertools import permutations

class P1():
    def foo(self):
        print('Parent 1')

    def bar(self):
        print('bar Parent 1')

class P2():
    # def foo(self):
    #     print('Parent 2')

    def bar(self):
        print('bar Parent 2')

class C1(P1,P2):
    pass
    # def foo(self):
    #     print('Child 1')

class C2(P1,P2):
    def foo(self):
        print('Child 2')
    
    def bar(self):
        print('bar Child 2')

class GC(C1,C2):
    pass
    # def foo(self):
    #     print('Grand Child') 
gc=GC()
print(isinstance(5,type(0)))
print(vars(gc))
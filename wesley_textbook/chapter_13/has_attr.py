class Name():
    'Testing class'
    count=0
    god=25
    def __init__(self,naam,age,loc):
        self.naam=naam
        self.age=age
        self.adr=loc
        self.god=100
        Name.count+=1

    def func(self):
        print(f'Name is {self.naam} {self.age} {self.adr}')
    
    def _display(self):
        print(f'Name is {self.naam} {self.age} {self.adr}')

    def __iadd__(self,val):
        self.age+=1
        self.func()

    def __add__(self,other):
        new_obj=Name(self.naam+' '+other.naam,self.age+other.age,'')
        return new_obj

    def call(self):
        print(self)

    def __del__(self):
        # print('deleted')
        Name.count-=1
    
    def show(cls):
        print(f'Object count:   {cls.count}')

    show=classmethod(show)

class Student(Name):

    Student_name_list=[]

    def __init__(self,naam,age,loc,dept):
        Name.__init__(self,naam,age,loc)
        self.dep=dept
        Student.Student_name_list.append(naam)
    
    
stud=Student('Abhishke',21,'Majali','CSE')

print(hasattr(stud,'adr'))
print(getattr(stud,'adr'))
print(setattr(stud,'adr','new_loc'))
print(getattr(stud,'adr'))





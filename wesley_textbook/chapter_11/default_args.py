def func(a,b=0,c=0,*t,**d):
    print(f' value of a is {a}')
    print(f' value of b is {b}')
    print(f' value of c is {c}')
    print(t)
    print(d)
    print('\n')


func(45,0,0,23,45,33,*(3,4,5,6))
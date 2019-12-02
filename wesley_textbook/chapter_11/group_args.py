def func(a,b,**d):
    "hello there"
    print(a+b)
    # print(type(c))
    # print(sum(c))
    print(d)
    
    
    

func(4,5,key=10,vl=10)
print(func.__doc__)
func.__doc__='hell is here'
print(func.__doc__)



def func():
    print('i was here')
    global s
    s=10
   

s=20
print(s,id(s))

func()
print(s,id(s))

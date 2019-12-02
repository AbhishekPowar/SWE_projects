l=[]
def push():
    l.append(input())

def pop():
    if len(l)==0:
        print('Stack Empty')
        return 0
    print(f'Removed {l.pop()}')

def display():
    print(l)

cmd={'push':push ,'pop':pop ,'display':display}

def stack():
    while (val:=input())!=quit:
        cmd[val]()

stack()



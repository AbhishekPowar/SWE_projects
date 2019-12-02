def check(func_name):
    def inside_func(a,b):
        if b == 0:
            print("Can't divide by zero")
            return
        func_name(a,b)
    return inside_func

@check
def div(a,b):
    return a/b




print(div(1,0))
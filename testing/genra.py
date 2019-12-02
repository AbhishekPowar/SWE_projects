import time
def time_it(func):
    def inside(l):
        start=time.time()
        func(l)
        end=time.time()
        print(f'Time taken by {func} is {end-start}',)
    return inside
@time_it
def main(limit):
    def fun():
        for i in range(limit):
            yield i*i
            
    sums=0
    for i in fun():
        sums+=i

@time_it
def main2(limit):
    def fun():
        l=[]
        for i in range(limit):
            l.append(i*i)
        return l
            
    sums=0
    for i in fun():
        sums+=i

limit=10000000
main(limit)
main2(limit)
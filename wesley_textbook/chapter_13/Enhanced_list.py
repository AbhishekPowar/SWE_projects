class newlist(list):
    def append(self,x):
        super().insert(0,x)

l=newlist()
for i in range(10):
    l.append(i)

print(l)

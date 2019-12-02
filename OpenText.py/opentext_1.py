input_list=list(map(int,input().split()))
m=int(input())
d=dict()
for i in input_list:
    val=d.setdefault(i,0)
    d[i]=val+1

ans=[]
l=sorted(d.keys(),key=d.get)
for i in l:
    for j in range(d[i]):
        ans.append(i)

# print(ans)
print(f'Answer : {len(set(ans[m:]))}')




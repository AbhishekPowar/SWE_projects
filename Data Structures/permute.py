def perm(arr,l,h):
    global k
    if l==h:
        k.append(arr)

    else:
        for i in range(len(arr)):
            arr[l],arr[i]=arr[i],arr[l]
            perm(arr,l+1,h)
            arr[l],arr[i]=arr[i],arr[l]
k=[]       
perm([1,2,3],0,2)
print(sorted(k))
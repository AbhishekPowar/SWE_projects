ans={}
for c in range(1,100+1):
    N=c

    d=dict()
    d=d.fromkeys(range(N),'Living')

    living_list = list(range(N))
    dead_list=[]
    dead=[]

    loop=len(bin(N)[2:])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
        
    k=0
    pdead=0
    while True:
        if pdead == N-1:
                break
        if d[k] == 'Living':
                while d[(k+1)%N] =='Dead':
                    k+=1
                d[(k+1)%N] ='Dead'
                pdead+=1
                if pdead == N-1:
                    break
        k+=1
        if k>=N:
            k=k%N    

    for i in d:
        if d[i] == 'Living':
            ans[N]=i+1

for c in ans:
    print('-'*30)
    print(f'|{str(c).center(15)}|{str(ans[c]).center(15)}|')
    
            


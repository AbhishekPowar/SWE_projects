def base(val=1,b=2):
    l=[]
    while val:
        bit=val%b
        if bit>=10:
            l.insert(0,str(chr(bit+55)))
        else:
            l.insert(0,str(bit))

        val//=b
    return l

def check(str,desc=None,low=0,high=9):
    if desc=='base' and len(str)==1 and str in ['0','1']:
        print('Base must be greater than 1')
        return False
    if str=='':
        print('Cant be Empty')
        return False
    num_list=[chr(i+48)for i in range(low,high+1)]
    for ch in str:
        if ch not in num_list:
            print(f'{ch} is not a number')
            return False
    return True

def main():   
    number_user=input('Num :')
    while True:
        if not check(number_user):
            number_user=input('Num :')
        else:
            break       
    number_user=int(number_user) 
    
    base_user=input('Base :')
    while True:
        if not check(base_user,'base'):
            base_user=input('Base :')
        else:
            break
    base_user=int(base_user)
    
    
    # base_user=int(input('Base :'))
    

    ans_list=base(number_user,base_user)
    print('Answer is    :',''.join(ans_list))

try:
    main()
except BaseException as id:
    print('Sorry error occured')

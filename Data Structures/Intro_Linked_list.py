class Node():
    def __init__(self,data=0):
        self.data=data
        self.next=None

class LinkedlList():
    def __init__(self):
        self.head=None 

def start():
    mylist=LinkedlList()
    print('Insert Command :     ',end='')
    while (val:=input())!='quit':
        val=val.lower()
        if val == 'insert':
            if mylist.head == None:
                print ('Insert Data :   ',end='')
                mylist.head =Node(input())
            else:
                print ('Insert Data :   ',end='')
                temp=Node(input())
                cur=mylist.head
                while cur.next!=None:
                    cur=cur.next

                cur.next=temp

        elif val == 'display':
            if mylist.head == None:
                print('Empty List')
            else:
                temp=mylist.head
                while temp!=None:
                    print(temp.data)
                    temp=temp.next

        elif val == 'delete':
            mylist.head = None
        
        elif val == 'pos':
            print ('Insert Data :   ',end='')
            temp=Node(input())
            cur=mylist.head
            if cur.next == None:
                cur.next=temp
            else:
                while cur.next.data < temp.data:
                    cur=cur.next
                    if cur.next == None:
                        cur.next=temp
                        break
                else:
                    temp.next = cur.next
                    cur.next = temp          
                
            
        else:
            print('Invalid Command')

        print('Insert Command :  ',end='')
start()

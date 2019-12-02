# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
phone_book={}
for i in range(N):
    #phone_book.update(input().split(" "))
    print(input().split())

for i in range(N):
    name=input()
    if name in phone_book:
        print("{}={}".format(name,phone_book.get(name)))
    else:
        print("Not Found")

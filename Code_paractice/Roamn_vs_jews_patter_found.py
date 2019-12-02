def calc(n):
    if list(bin(n)[2:]).count('1') == 1:
        return 1
    else:
        return calc(n-1)+2

x=int(input())
print(calc(x))    
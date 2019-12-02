import time
def main():
    import re

    str = "WoW!ItSCoOWoWW"
    sub='oW'
    occ=0
    sl=len(sub)//2
    while True:
        x=re.findall(sub,str)
        occ+=len(x)
        if x==[]:
            break
        str=re.sub(sub,sub[:sl],str)

    print(occ)

start=time.time()
main()
end=time.time()
print(end-start)
# string = "WoW!ItSCoOWoWW"
# sub_string='oW'

string = "ABCDCDC"
sub_string='CDC'
occ=0
sl=len(sub_string)
for i in range(len(string)-sl+1):
    val=string.find(sub_string,i,i+sl)
    if val!=-1:
        occ+=1

print( occ) 
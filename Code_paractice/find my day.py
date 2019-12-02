def find_my_year():
    ins=list(map(int,input().split('-')))
    d=ins[0]
    m=ins[1]-1
    y=ins[2]
    table_months=[1,4,4,0,2,5,0,3,6,1,4,6]
    table_years=[6,4,2,0]
    x=table_years[y%4]
    h_years=y-y%100
    value=(x+y%h_years+((y%h_years)//4)+table_months[m]+d)%7
    day=['sat','sun','mon','tues','wed','thur','fri']
    print(day[value]+'day')

for i in range(10):
    find_my_year()

    

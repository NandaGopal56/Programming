
import re
date='2014-10-10'

find = re.match('\d{4}-\d{2}-\d{2}' , date)

if find:
    date_str=date.split('-')
    i=0
    date=[]
for j in date_str:
        date.append(int(j))
        i+=1
if date[1] == 2:
    if date[0] % 4 == 0:
        if date[2] <= 29:
             print('date is valid')
    else:
        if date[2]<=28:
            print('date is valid')
elif date[1] == 1 or date[1] == 3 or date[1] == 5 or date[1] == 7 or date[1] == 8 or date[1] == 10 or date[1] == 12:
    if date[2] <= 31:
        print('date is valid')
else:
    if date[2] <= 30:
        print('date is valid')


#no of days calculation from current date to a given date

cd=int(input("enter cd: "))
cm=int(input("enter cm: "))
cy=int(input("enter cy: "))

dd=int(input("enter dd: "))
dm=int(input("enter dm: "))
dy=int(input("enter dy: "))

#day calculation

if cd>=dd:
    d=cd-dd
else:
    cm=cm-1
    if cm in [1,3,5,7,8,10,12]:
        cd=cd+31
    elif cm in [4,6,9,11]:
        cd=cd+30
    elif cm==2 and cy%4==0:
        cd=cd+29
    else:
        cd=cd+28
    d=cd-dd
#month calculation

if cm>=dm:
    m=cm-dm
else:
    cy=cy-1
    cm=cm+12
    m=cm-dm
#year calculation
y=cy-dy

print(d,"days",m,"months",y,"years")
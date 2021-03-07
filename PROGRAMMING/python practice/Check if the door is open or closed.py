def checkDoorStatus(N):
    doors = []
    for i in range(N):
        doors.append(1)
    print(doors)
    for i in range(2, N+1):
        for j in range(1, len(doors)+1):
            if j%i == 0:
                if doors[j-1] == 0:
                    doors[j-1] = 1
                else:
                    doors[j-1] = 0
    print(doors)

checkDoorStatus(5)

'''
https://practice.geeksforgeeks.org/problems/check-if-the-door-is-open-or-closed2013/1/?company[]=TCS&company[]=TCS&page=1&query=company[]TCSpage1company[]TCS#

'''
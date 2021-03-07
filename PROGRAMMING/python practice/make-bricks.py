def make_bricks(small, big, goal):
    if small*1==goal:
        return True
    if big*5==goal:
        return True
    for i in range(big):
        if goal>=5:
            goal=goal-5
        elif goal == 0:
            return True
        elif goal<5:
            break
    for i in range(small):
        if goal!=0:
            goal = goal-1
        if goal ==0:
            return True
    return False
    
print(make_bricks(3,1,9))

'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops
'''
'''
make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
'''
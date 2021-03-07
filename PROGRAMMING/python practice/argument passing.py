def first(*things):
    print(things,type(things))
def second(**item):
    print(item,type(item))

if __name__=='__main__':
    first(10,20,30)
    second(a=10,b=20)
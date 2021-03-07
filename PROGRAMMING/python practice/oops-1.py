class test:
    pass

def main():
    obj1=test()
    obj2=test()
    obj3=test()

    print('address of class: ',id(test))
    print('address of class: ', id(obj1.__class__))
    print('address of class: ', id(obj2.__class__))
    print('address of class: ', id(obj3.__class__))

    print('address of obj1: ', id(obj1))
    print('address of obj2: ', id(obj2))
    print('address of obj3: ', id(obj3))

main()
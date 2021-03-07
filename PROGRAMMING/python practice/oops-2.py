class test:
    pass

def main():
    obj1=test()
    obj2 = test()
    obj3 = test()

    test.a=10
    obj1.x=20
    obj2.y=30
    obj3.z=40

    print('memory of class: ',test.__dict__)
    print('memory of obj1: ',obj1.__dict__)
    print('memory of obj2: ', obj2.__dict__)
    print('memory of obj3: ', obj3.__dict__)

    print(test.a)
    print(obj1.a)
    print(obj2.a)
    print(obj3.a)

    print()

    print(obj1.x)
    print(obj2.y)
    print(obj3.z)

    print()

    obj1.a=100000000

    print('memory of obj1: ',obj1.__dict__)

    print()

    print(test.a)
    print(obj1.a)
    print(obj2.a)
    print(obj3.a)

    print()

    print(obj1.x)
    print(obj2.y)
    print(obj3.z)
    #print(obj2.x)  , 'test' object has no attribute 'x'

if __name__ == '__main__':
    main()
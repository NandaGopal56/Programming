class test:
    def m1(self):
        print('i am non static method')

    @classmethod
    def m2(cls):
        print('i am class method')

    @staticmethod
    def m3():
        print('i am static method')

def main():
    obj=test()

    test.m1(obj)
    obj.m1()

    test.m2()
    obj.m2()

    test.m3()
    obj.m3()

main()
def main():
    print("i am main")
    def fun():
        print("i am local fun to main function")
    fun()
    bbsr(fun)

def bbsr(formal_var):
    print("i am bsr")
    formal_var()

main()

"""
only in python function can be passed as an argument also so it is known as first class object
a function can be declared inside another sunction also and that is known as local function 
"""
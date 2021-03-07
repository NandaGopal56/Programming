var=10
def main():
    #  global var   #just check this line to validate
    var+=10   # it will give error because it is not declared as global inside the fuction befor modifing it
    print("i am main",var)
    bbsr()

def bbsr():
    print("i am bbsr",var)

main()

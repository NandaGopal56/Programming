var=10
def main():
    global var
    var+=10
    print("i am main",var)
    bbsr()

def bbsr():
    print("i am bbsr",var)

main()
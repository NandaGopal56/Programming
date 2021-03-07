def main():
    actual_parameter=10
    print("actual_parameter",id(actual_parameter),actual_parameter)
    bbsr(actual_parameter)
    
    print(actual_parameter,id(actual_parameter))

def bbsr(formal_parameter):
    print("formal-parameter",id(formal_parameter),formal_parameter)
    formal_parameter+=10

    print(formal_parameter)

main()
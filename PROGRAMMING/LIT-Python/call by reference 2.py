def main():
    actual_parameter=[11,22,33]
    print("actual_parameter",id(actual_parameter),actual_parameter)
    bbsr(actual_parameter)

    print(actual_parameter,id(actual_parameter))

def bbsr(formal_parameter):
    print("formal parameter",id(formal_parameter),formal_parameter)
    formal_parameter.append(44)
    formal_parameter.append(55)

main()

"""
in list function argument passing and call always works as call by reference
"""
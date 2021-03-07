while True:
    no = int(input("enter a number: "))
    record = no
    rev = 0
    while no != 0:
        last = no % 10
        rev = rev * 10 + last
        no = no // 10

    if record == rev:
        print("number is pallindrome")
    else:
        print("number is not pallindrome")
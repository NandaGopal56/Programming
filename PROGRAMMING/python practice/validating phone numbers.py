def check(l):
    check = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    for no in l:
        count = 0
        if len(no) == 10:
            if no[0] == '7' or no[0] == '8' or no[0] == '9':
                for digit in no:
                    if digit in check:
                        count += 1
                if count == 10:
                    print("YES")
                else:
                    print("NO")
            else:
                print("NO")

        else:
            print('NO')


if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(input())
    check(l)



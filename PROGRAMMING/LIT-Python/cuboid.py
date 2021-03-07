def draw(x, y, z, n):
    final = []

    for i in range(x + 1):

        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                    lsit = []
                    list = [i, j, k]
                    final.append(list)

    print(final)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    draw(x, y, z, n)


"""
#alternate code

def draw(x, y, z, n):
    final = []

    for i in range(x + 1):

        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != n:
                     list1=[]
                     list1.append(i)
                     list1.append(i)
                     list1.append(i)
                     final.append(list1)

    print(final)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    draw(x, y, z, n)



"""
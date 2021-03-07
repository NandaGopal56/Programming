if __name__ == '__main__':
    l = []
    N = int(input())

    for i in range(N):
        command = input()
        command = command.split(' ')
        if command[0] == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif command[0] == 'append':
            l.append(int(command[1]))
        elif command[0] == 'print':
            print(l)
        elif command[0] == 'remove':
            l.remove(int(command[1]))
        elif command[0] == 'sort':
            l.sort()
        elif command[0] == 'pop':
            l.pop()
        elif command[0] == 'reverse':
            l.reverse()

"""
---INPUT---
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print


---OUTPUT---

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
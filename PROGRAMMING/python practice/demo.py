n = int(input())
actual = []
mini = []
for i in range(n):
    actual.append(int(input()))
for i in range(n):
    mini.append(int(input()))

print(max(max(actual), max(mini)))
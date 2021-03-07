class Stack:
    def __init__(self):
        self.list = []
    def __str__(self):
        if self.list != []:
            values = self.list.copy()
            values.reverse()
            values = [str(x) for x in values]
            x = '\n'.join(values)
            return x
        else: return 'The stack is empty !'
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self, data):
        self.list.append(data)
        return "The element was inserted successfully"
    def pop(self):
        if self.list == []:
            print('The stcak is empty')
        else:
            self.list.pop()
    def peek(self):
        if self.list == []:
            print("The stack is empty")
        else:
            return self.list[-1]
    def delete(self):
        self.list = []

s1 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print(s1)
print('peek', s1.peek())
s1.delete()
print(s1)



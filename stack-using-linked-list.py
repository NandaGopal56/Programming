class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.ref
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    def __str__(self):
        values = [str(x.data) for x in self.LinkedList]
        return '\n'.join(values)
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else: return False
    def push(self, data):
        node = Node(data)
        node.ref = self.LinkedList.head
        self.LinkedList.head = node
    def pop(self):
        if self.LinkedList.head is None:
            print("stack is empty")
        else:
            nodeValue = self.LinkedList.head.data
            self.LinkedList.head = self.LinkedList.head.ref
            return nodeValue
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            return self.LinkedList.head.data
    def delete(self):
        self.LinkedList.head = None

s1 = Stack()
s1.push(10)
s1.push(20)
print("printing stack:")
print(s1)
print('peek', s1.peek())
print("printing stack:")
print(s1)
s1.pop()
print("printing stack:")
print(s1)

        
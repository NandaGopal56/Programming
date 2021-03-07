class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.ref = node
        self.head = node
        self.tail = node
        self.traverserCSLL()
    def insertCSLL(self, data, location):
        if self.head is None:
            print("The Circular linked list does not exist")
        else:
            new_node = Node(data)
            if location == 0:
                new_node.ref = self.head
                self.head = new_node
                self.tail.ref = new_node
            elif location == 1:
                new_node.ref = self.tail.ref
                self.tail.ref = new_node
                self.tail = new_node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.ref
                    index += 1
                nextNode = tempNode.ref
                tempNode.ref = new_node
                new_node.ref = nextNode
        self.traverserCSLL()

    def traverserCSLL(self):
        if self.head is None:
            print("The circular linked list does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.data, end = ' ')
                tempNode = tempNode.ref
                if tempNode == self.tail.ref:
                    break
        print()
    def searchCSLL(self, data):
        if self.head is None:
            print("Circular linked list does not exist")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.data == data:
                    print(f'Data found in the CSLL - {data}')
                tempNode = tempNode.ref
                if tempNode == self.tail.ref:
                    print(f'The data is not found inside the CSLL')
    def deleteNode(self, location):
        if self.head is None:
            print("Circular linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.ref = self.head = self.tail = None
                else:
                    self.head = self.head.ref
                    self.tail.ref = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.ref = self.head = self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.ref == self.tail:
                            break
                        node = node.ref
                    node.ref = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.ref
                    index += 1
                nextNode = tempNode.ref
                tempNode.ref = nextNode.ref  
        self.traverserCSLL()              
    def deleteEntireCSLL(self):
        self.head = self.tail.ref = self.tail = None
        print("deleted the CSLL")

csll1 = CircularLinkedList()
csll1.createCSLL(100)
csll1.insertCSLL(11, 0)
csll1.insertCSLL(111, 0)
csll1.insertCSLL(22, 1)
csll1.insertCSLL(222, 1)
csll1.insertCSLL(55, 3)
csll1.insertCSLL(555, 4)
csll1.deleteNode(0)
csll1.deleteNode(1)
csll1.deleteNode(3)
csll1.deleteEntireCSLL()
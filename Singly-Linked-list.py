class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Traversing through the linked list
    def traverseSLL(self):
        if self.head is None:
            print("Singly linked list is empty !!")
        else:
            n = self.head
            while n is not None:
                print(n.data, end = " ")
                n = n.ref
        print()

    #Inserting to the linked list : 0-Beginning, 1-End, any other value of location is position except 0 & 1
    def insertSLL(self, data, location):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                new_node.ref = self.head
                self.head = new_node

            elif location == 1:
                new_node.ref = None
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

    #Searching for an element in the linked list
    def searchSLL(self, data):
        if self.head is None:
            print("The list does not exist")
        else:
            node = self.head
            while node is not None:
                if node.data == data:
                    print(f'Data found = {data}')
                    return None
                node = node.ref
            print("Data not found in the linked list")
    def deleteNode(self, location):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.ref
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.ref == self.tail:
                            break
                        node = node.ref
                    node.ref = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.ref
                    index += 1
                nextNode = tempNode.ref
                tempNode.ref = nextNode.ref
        self.traverseSLL()

    def deleteEntireSLL(self):
        if self.head is None:
            print("Linked list does not exist")
        else:
            self.head = self.tail = None
        print("deleter all the items of the linked list")
        self.traverseSLL()

sl1 = SinglyLinkedList()
#insert at the beginning
sl1.insertSLL(1, 0)
sl1.insertSLL(11, 0)
#insert at the end
sl1.insertSLL(2, 1)
sl1.insertSLL(22, 1)
#insert at specific position
sl1.insertSLL(31, 2)
sl1.insertSLL(32, 3)
#Traversing the linked list
sl1.traverseSLL()
#searching for a element
#sl1.searchSLL(int(input('Enter a data to search in the linked list: ')))

#Delete an item from the linked list
sl1.deleteNode(3)

#delete the entire linked list
sl1.deleteEntireSLL()
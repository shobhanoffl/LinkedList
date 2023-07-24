class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def removeFromEnd(self):
        prev = self.head
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        tail = prev
        tail.next = None
        self.length -= 1

    def printLL(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


ll = LinkedList()

ll.append(5)
ll.append(3)
ll.append(8)

ll.printLL()

ll.removeFromEnd()

ll.printLL()

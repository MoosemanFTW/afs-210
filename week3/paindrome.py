class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None #head
        self.size = 0
        self.length = 0




class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enque(self, data):
        new_node = Node(data)
        if self.head is None:         
            self.head = new_node
            return      
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def deque(self):
        if self.head is None:
            print('list is empty')
        else:
            new_head = self.head.next
            self.head = new_head
            self.length -= 1

    def isEmpty(self):          #if empty returns TRUE
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        return self.length

    def peek(self):
        return self.head

my_queue = Queue()
print(my_queue.size())
from operator import index, indexOf


class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        new_node = Node(data) 
        if self.head is None: 
            self.head = new_node 
            self.tail = self.head 
        else: 
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node 

            self.count += 1

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def getIndex(self, index):
        curr = self.head
        end = self.tail
        i = 0
        while curr is not end:
            if (i == index):
                return curr
            else:
                i += 1
                curr = curr.next
        print(curr.data)
        if curr == self.tail:
            if index == i +1:
                return curr
            else:
                return False
        # return False
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if self.head is None:
            print("List is empty")
            return
        else:
            curr = self.getIndex(index)
            if curr:
                new_node = Node(data)
                if curr:
                    if not curr.prev:
                        self.addFirst(data) 
                    elif not curr.next:
                        self.addLast(data)   
                    else:
                        curr.prev.next = new_node
                        new_node.prev = curr.prev
                        new_node.next = curr
                        curr.prev = new_node
            else:
                print('OUT OF LIMITS')
        

    def indexOf(self, data):
    #     # Search through the list. Return the index position if data is found, otherwise return -1    
        curr = self.head
        end = self.tail
        i = 0
        while curr is not end:
            if (curr.data == data):
                return i
            else:
                i += 1
                curr = curr.next
        print(i)
        if curr == self.tail:
            if curr.data == data:
                return i
            else:
                return False


    # def add(self, data) -> None:
    #     # Append an item to the end of the list
    #     self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        print(myStr)



list = DoublyLinkedList()
list.addLast('May')
list.addLast('the')
list.addLast('Force')
list.addLast('be')
list.addLast('with')
list.addLast('you')
list.addLast('!')
list.__str__()
print(list.indexOf('with'))
list.addAtIndex('us', 5)
list.addAtIndex('all', 6)
list.delete('you')
list.__str__()
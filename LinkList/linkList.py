# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data=None, next=None):
        self.data = data  # assign data
        self.next = next  # initialize next


# Linked List class
class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(12)
    ll.insert_at_begining(24)
    ll.insert_at_begining(34)
    ll.insert_at_end(7)
    ll.insert_at_begining(43)
    ll.print()

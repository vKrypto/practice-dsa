

class Node(object):

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None



class  DoublyLinkedList(object):
    ''' docstring for  LinkedList.'''

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail =None

    def size(self):
        ''' o(1): simple returns attribute '''
        return self.size

    def calculate_size(self):
        ''' O(n): travers all item and calculate size again'''
        start = self.head
        size = 0
        while  start:
            size =+ 1
            start = start.next
        self.size = size
        return size

    def insertStart(self,data):
        '''O(1): insert item at start(head) '''
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head

    def get_last_node(self):
        '''O(n): returns the last item of linked list'''
        start = self.head
        while start:
            start = start.next
        return start

    def insertLast(self,data):
        ''' O(n): insert node at last '''
        self.size =+ 1
        new_node = Node(data)
        last_node = self.get_last_node()
        last_node.next = new_node

    def search_data(self,data):
        ''' O(n): return the first matched node unless -1'''
        start = self.head
        while  start.data != data or start.next:
            start = start.next
        return start if start.data == data else -1

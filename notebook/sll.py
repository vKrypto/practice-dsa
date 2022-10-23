'''

linked list implementation from scatch

'''

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class  LinkedList:
    '''docstring for  LinkedList.'''

    def __init__(self):
        self.head = None
        self.size = 0

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
        last_node = get_last_node(self)
        last_node.next = new_node

    def search_data(self,data):
        ''' O(n): return the first matched node unless -1'''
        start = self.head
        while  start.data != data and start.next:
            start = start.next
        return start if start.data == data else -1

    def traverse(self):
        '''O(n): print each node '''
        start = self.head
        while start.next:
            start = start.next
            print(start, '>>>>>',start.data)

    def remove(self,data):
        '''' O(n):  search node by data and remove that by returnin gnode object '''
        if self.head is None:
            return None
        first = second = self.head
        while second.data != data and first.next:
            second = first.next
            start = start.next
            if second.data == data:
                break
        if first.next is None:
            return None
        first.next = second.next
        return second





''' create ing a linked list of 1000  node '''
def get_hash_data(num):
    return num**2

ll = LinkedList()
for i in range(1000):
    data = get_hash_data(i)
    ll.insertStart(data)

print(ll)
ll.traverse()

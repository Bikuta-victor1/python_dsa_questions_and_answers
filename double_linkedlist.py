class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList: 
    def __init__(self):
        
        self.head = None
      
      # def print_
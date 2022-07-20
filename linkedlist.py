# Node Class that represent an illusion element
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    # Linked List with an head variable that points to the head of the linkedlist
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        # new node value is head of current list
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        # new node value is head of current list
        if self.head is None:
            self.head = Node(data, self.head)
            return
        
        itr = self.head # the first node in the linked list
        # if iter.next has some value,  i keep iterating
        
        while itr.next:
            itr = itr.next
        # when iter.next becomes null ,that is the last element, so we give it a new node
        itr.next = Node(data, None)
        
    def insert_values(self, data_list):
        self.head = None # initializing the linkedlist to empty
        for data in data_list:
            self.insert_at_end(data)
        
    def print(self):
        # If first head(first node) is empty
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head  # the first node in the linked list
        llstr = ''
        
        # If first head is not empty
        while itr:
            # Keep adding to the linked list
            llstr += str(itr.data) + '--->'
            itr = itr.next
        
        print(llstr)
        
    def get_length(self):
        count = 0
       
        itr = self.head  # the first list in the linked list
        while itr:
            count += 1
            itr = itr.next
            
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
        
            itr = itr.next  # iterating through the node
            count += 1
            
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["78", "89", "99", "899"])
    ll.print()
    ll.insert_at(0, "Light")
    ll.print()
    

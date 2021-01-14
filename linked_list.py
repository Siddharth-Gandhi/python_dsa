class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __print__(self):
        print(self.data)

class Linked_List:
    def __init__(self):
        self.head = None
    
    def __insert__(self, data):
        
        if self.head == None:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def insert(self, data):
        self.head.__insert__(data)
    
    
class Node(object):
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self, val):
        self.head = Node(val)
    
    def printList(self):
        Headval = self.head
        while Headval is not None:
            print(Headval.val)
            Headval = Headval.next    

    def reversePrintList(self):
        Headval = self.head
        while Headval.next is not None:
            Headval = Headval.next

        print(Headval.val)
        while Headval.prev is not None:
            print(Headval.prev.val)
            Headval = Headval.prev

    def addInBetween(self, middle_node, value):
        Newnode = Node(value)

        if middle_node.next == None:
            middle_node.next = Newnode
            Newnode.prev = middle_node

        else: 
            middle_node_next = middle_node.next
            middle_node_next.prev = Newnode
            middle_node.next = Newnode
            Newnode.prev = middle_node
            Newnode.next = middle_node_next

    def addAtTail(self, value):
        Newnode = Node(value)
        Headval = self.head
        while Headval.next is not None:
            Headval = Headval.next
        
        Headval.next = Newnode
        Newnode.prev = Headval

    def delete(self, value):
        Headval = self.head
        
        while Headval.next is not None:
            if Headval.val == value:
                Headval_prev = Headval.prev
                Headval_next = Headval.next
                Headval_prev.next = Headval.next
                Headval_next.prev = Headval.prev
                             
            Headval = Headval.next

        if Headval.val == value:
            Headval_prev = Headval.prev
            Headval_prev.next = None
            Headval = None

        



print('------------------Initialization---------------------')
l = DoublyLinkedList('Sun')
l.printList()

print('------------------Add In Between---------------------')
l.addInBetween(l.head, 'Mon')
l.printList()

print('------------------Add At Tail------------------------')
l.addAtTail('Tue')
l.printList()

print('------------------Add At Tail------------------------')
l.addAtTail('Wed')
l.printList()

print('------------------Add At Tail------------------------')
l.addAtTail('Mon')
l.printList()
print('------------------Reverse Print------------------------')
l.reversePrintList()

print('--------------------Delete---------------------------')
l.delete('Mon')
l.printList()
print('------------------Reverse Print------------------------')
l.reversePrintList()


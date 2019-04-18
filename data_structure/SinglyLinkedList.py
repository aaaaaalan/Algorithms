'''

Author: AOLAN SUN
'''

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self, data=None):
        self.head = Node(data)

    def printList(self):
        Headval = self.head
        if Headval is None:
            print('Empty LinkedList.')
        while Headval is not None:
            print(Headval.data)
            Headval = Headval.next
        
    def reversePrintList(self):
        tail = None
        while tail is not self.head:
            curr = self.head
            while curr.next is not tail:
                curr = curr.next
            tail = curr
            print(tail.data)

    def addInBetween(self, middle_node, value):
        if middle_node is None:
            print('The mentioned node above is absent.')
            return 

        NewNode = Node(value)
        NewNode.next = middle_node.next
        middle_node.next = NewNode

    def addAtTail(self, value):
        Headval = self.head
        if Headval is None:
            self.head = Node(value)
        
        while Headval is not None:
            head_next = Headval.next
            if head_next is not None:
                Headval = Headval.next
            else:
                NewNode = Node(value)
                Headval.next = NewNode
                return 
            
    def delete(self, value):
        curr = self.head
        if curr.data == value:
            self.head = curr.next
            curr = None
            return
        
        curr_next = curr.next
        while curr_next is not None:
            if curr_next.data == value:
                curr.next = curr_next.next
                
            else:
                curr = curr.next
             
            curr_next = curr.next
                
        return
            
        


print('----------------- Initialization --------------------')
l = SinglyLinkedList('Sun')
l.printList()

Sunday = Node('Sun')
print('---------------- Add In Between ---------------------')
l.addInBetween(l.head, 'Mon')
l.printList()
print('---------------- Add In Between ---------------------')
l.addInBetween(l.head.next, 'Tue')
l.printList()
print('---------------- Add At Tail ---------------------')
l.addAtTail('Wed')
l.printList()
print('---------------- Add At Tail ---------------------')
l.addAtTail('Thu')
l.printList()
print('---------------- Add At Tail ---------------------')
l.addAtTail('Tue')
l.printList()
print('---------------- Reverse Print -------------------')
l.reversePrintList()

print('------------------- Delete ---------------------------')
l.delete('Tue')        # 由于 if return 只能删除第一个Tue
l.printList()
print('---------------- Reverse Print -------------------')
l.reversePrintList()

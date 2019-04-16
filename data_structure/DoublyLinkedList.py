class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
        self.previousval = None

class DLinkedList:
    '''
    Doubly Linked List Implementation
    traverse the list in forward direction.
    print the value of the next data element by assigning the pointer of the next node to the current data element
    '''
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

        # Update the new nodes next val to existing head node 
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return 
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def InBetween(self, middle_node, newdata):
        if middle_node is None:
            print("The mentioned node is absent.")
            return
        
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):
        HeadVal = self.headval

        if HeadVal is not None:
            if HeadVal.dataval == Removekey:
                self.headval = HeadVal.nextval
                HeadVal = None
                return

        while HeadVal is not None:
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if HeadVal == None:
            return
      
        prev.nextval = HeadVal.nextval
        HeadVal = None



list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first node to the second node
list1.headval.nextval = e2

# LInke second node to the third node
e2.nextval = e3


# Traversing a Linked List
print("-------------")
list1.listprint()

# Add node at the beginning
list1.AtBeginning("Sun")
print("-------------")
list1.listprint()

# Add node at the end
list1.AtEnd("Thu")
print("-------------")
list1.listprint()

# Add node in between
list1.InBetween(list1.headval.nextval, "Fri")
print("-------------")
list1.listprint()

# Remove Node Tue
list1.RemoveNode("Tue")
print("-------------")
list1.listprint()

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashmap = {}
        i = 0
        
        if head.next == None:
            return head
        else:
            while head.next is not None:
                hashmap[i] = head
                head = head.next 
                i += 1
        
            length = i + 1
            
            if length % 2 == 1:
                middle_index = (length - 1) / 2

            else:
                middle_index = length / 2

            return hashmap[middle_index]
        
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h1 = head
        h2 = head 
        while h2.next is not None and h2.next.next is not None:
            h1 = h1.next
            h2 = h2.next.next
            
        if h2.next is not None:
            h1 = h1.next
            
        return h1

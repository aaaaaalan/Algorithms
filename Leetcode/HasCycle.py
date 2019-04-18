#141
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hashmap = {}
        i = 0 
        while head:
            # head is a node here, which can help just if the pointer points back to the nodes in the list.
            if head in hashmap:
                return True
            else:
                hashmap[head] = i
                head = head.next
                i += 1
        
        return False

#160

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        curr_headA = headA
        while curr_headA:
            curr_headB = headB
            while curr_headB:
                if curr_headA == curr_headB:
                    return curr_headA
                else:
                    curr_headB = curr_headB.next
            
            curr_headA = curr_headA.next
        
        return None
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
    
        address = set()
        while headA:
            address.add(headA)
            headA = headA.next
        while headB:
            if headB in address:
                return headB
            headB = headB.next
        return None

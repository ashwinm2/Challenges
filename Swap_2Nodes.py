# Swap 2 Nodes

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count  = 0
        if head is not None:
            back = head
            head = head.next    
            while head is not None:
                if count % 2 == 0:
                    curr = head.val
                    prev = back.val
                    swap = curr
                    curr = prev
                    prev = swap
                    head.val = curr
                    back.val = prev
                
                count += 1
                back = head
                head = head.next    
              
        return temp
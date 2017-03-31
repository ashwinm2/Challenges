# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        temp = head
        while head != None:
            count += 1
            head = head.next
        
        if count == 0 or count == 1:        
            return None
        else:
            #print "length ", count
            pos = count - n + 1
            n = 1
            #print "Here", pos, n
            if pos != n:
                prev = None
                head = temp
                while n < pos:
                    prev = head
                    head = head.next
                    n += 1
                #print prev.val, head.val
                prev.next = head.next
            else:
                temp = temp.next
        return temp
        
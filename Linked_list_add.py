# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        temp = l1
        while l1 != None and l2 != None:
            l1.val = l1.val + l2.val + carry
            #print "S", l1.val, l2.val
            if l1.val >= 10:
                carry = l1.val / 10
                l1.val = l1.val % 10
            else:
                carry = 0
            prev = l1
            l1 = l1.next
            l2 = l2.next
            
        if l2 != None:
            prev.next = l2
            while carry != 0:
                l2.val = l2.val + carry
                carry = 0
                if l2.val >= 10:
                    carry = l2.val / 10
                    l2.val = l2.val % 10
                    if l2.next == None:
                        node = ListNode(carry)
                        l2.next = node
                        carry = 0
                    else:
                        l2 = l2.next
        elif l1 != None:
            while carry != 0:
                l1.val = l1.val + carry
                #print "Where", l1.val
                carry = 0
                if l1.val >= 10:
                    carry = l1.val / 10
                    l1.val = l1.val % 10
                    if l1.next == None:
                        node = ListNode(carry)
                        l1.next = node
                        carry = 0
                    else:
                        l1 = l1.next
        elif carry != 0:
            node = ListNode(carry)
            prev.next = node
        return temp
            
# Rotation Linked List
class Solution(object):
    def rotateRight(self, head, k):
        temp = head
        length = 0
        while temp != None:
            temp = temp.next
            length += 1
        
        if k > length and length > 0:
            k = k % length
        
        if length < 2 or length == k or k == 0:
            return head
        elif length == 2:
            temp = head
            trail = temp.next
            trail.next = temp
            temp.next = None
            return trail
        else:
            temp = head
            while k < length - 1:
                temp = temp.next
                k += 1
            trail = ListNode(temp.next.val)
            trail.next = temp.next.next
            trailt = trail
            while trailt.next != None:
                trailt = trailt.next
            trailt.next = head
            temp.next = None
            return trail
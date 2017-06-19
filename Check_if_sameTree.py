# Check if same tree
class Solution(object):
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
        return False    
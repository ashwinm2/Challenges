# Permutation Sequence
class Solution(object):
    def getPermutation(self, n, k):
        target = []
        for x in range(1, n + 1):
            target.append(x)
        k -= 1
        index = 0
        while n > 1:
            order = n - 1
            ordrval = self.permute(order)
            # print k / float(ordrval)
            if k / float(ordrval) < 1.0:
                index += 1
                n -= 1
            else:
                jndex = k / ordrval
                k = k % ordrval
                n -= 1
                # print "Remainder", k, "order", n,"val", ordrval, "index", index, jndex 
                target, index = self.swap(target, index, index + jndex)
        
        target = [str(x) for x in target]
        return "".join(target)
    
    def swap(self, target, index, jndex):
        temp = target[jndex]
        del target[jndex]
        target.insert(index, temp)
        return target, index + 1
    
    def permute(self, num):
        total = 1
        while num > 1:
            total *= num
            num -= 1
        return total
        
        
    
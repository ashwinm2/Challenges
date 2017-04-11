# Generate_parantheses
from copy import deepcopy
    
class Solution(object):
    def __init__(self):
        self.final = []
        
    def result(self, comb):
        self.final.append(comb)
    
    def compute(self, ele, stack, n, q, balance):
        temp = deepcopy(stack)
        temp.append(ele)
        if len(temp) < 2 * q:
            if n > 0:
                if balance > 0:
                    self.compute("(", temp, n-1, q, balance + 1)
                    self.compute(")", temp, n, q, balance - 1)
                else:
                    self.compute("(", temp, n-1, q, balance + 1)
            else:
                self.compute(")", temp, n, q, balance - 1)
        else:
            self.result("".join(temp))


    def generateParenthesis(self, n):
        self.compute("(", [], n-1, n, 1)
        return self.final
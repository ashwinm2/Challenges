# Longest Valid  parantheses

class Solution(object):
    def longestValidParentheses(self, s):
        l = len(s)
        big = 0
        stack = []
        for index in range(0, l):
            if s[index] == "(":
                stack.append(index)
            else:
                if stack != [] and s[stack[-1]] == "(":
                    #print "Stack", stack, "Val", big
                    stack.pop()
                    if stack == []:
                        temp = -1
                    else:
                        temp = stack[-1]
                    
                    if big < index - temp:
                        big = index - temp
                        #print "Change big", big 
                else:
                    stack.append(index)
                    
        return big
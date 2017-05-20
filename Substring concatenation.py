# Substring concatenation
import copy

class Solution(object):
    def compute(self, allw, index, s, count, wordn, wordl):
        length = len(s)
        jndex = index
        while count < wordn:
            temp = s[jndex: jndex + wordl]
            #print "Word", temp, "Index", jndex
            #print allw
            if temp in allw:
                if allw[temp] == 0:
                    return -1
                else:
                    allw[temp] -= 1
            else:
                return -1
            count += 1
            jndex += wordl
        return jndex
    
    def findSubstring(self, s, words):
        if words == []:
            return []
        else:
            length = len(s)
            wordl = len(words[0])
            wordn = len(words)
            final = []
            
            allw = {}
            for each in words:
                if each not in allw:
                    allw[each] = 1
                else:
                    allw[each] += 1
            
            if len(allw.keys()) == 1:
                no = allw[words[0]]
                new = words[0] * no
                del allw[words[0]]
                allw[new] = 1
                wordl = no * len(words[0])
                wordn = 1
            
            #print allw
            index = 0
            while index < length:
                if wordl >= length:
                    temp = s[index:]
                else:
                    temp = s[index: index + wordl]
                #print temp, s[index:]
                if temp in allw:
                    dic = copy.deepcopy(allw)
                    result = self.compute(dic, index, s, 0, wordn, wordl)
                    #print "Iterations", index, result
                    if result != -1:
                        final.append(index)
                index += 1 
            return final
class Solution(object):
    def longestCommonPrefix(self, strs):
        final = ""
        longest = 0
        l_list = len(strs)
        
        if l_list > 1:
            l_base = len(strs[0])
            index = 0
            if l_base > 0:
                while index < l_base: 
                    alpha = {}
                    base = strs[0][:index+1]
                    print "Check", base
                    for ele in range(0, l_list):
                        if strs[ele] != "":
                            temp = strs[ele][:index + 1] 
                            if temp not in alpha:
                                alpha[temp] = 1
                                
                        else:
                            return ""
                    if len(alpha.keys()) > 1:
                        return final
                    final = temp
                    index += 1

            else:
                return ""
        else:
            if l_list == 1:
                final = strs[0]
        return final

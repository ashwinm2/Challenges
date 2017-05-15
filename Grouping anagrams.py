# Grouping anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        elif len(strs) == 1:
            return [strs]
        else:
            final = []
            total = {}
            count = 0
            for each in strs:
                temp = "".join(sorted(each))
                if temp not in total:
                    total[temp] = count
                    final.append([each])
                    count += 1
                else:
                    final[total[temp]].append(each)
            
            
            return final
                
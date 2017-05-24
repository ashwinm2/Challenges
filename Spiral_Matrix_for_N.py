# Spiral Matrix for N
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n != 0:
            final = [[0 for b in range(n) ] for a in range(n)]
            length = n
            breadth = n
            count = 0
            total = length * breadth
            index = 0
            jndex = 0
            while count < total:
                x = 0
                while x < breadth and count < total:
                    count += 1
                    final[jndex][index] = count
                    index = index + 1
                    x += 1
                # print "Check", jndex, index, final
                length -= 1
                jndex += 1
                index -= 1
                
                
                
                x = 0
                while x < length and count < total:
                    count += 1
                    final[jndex][index] = count
                    jndex += 1
                    x += 1
                breadth -= 1
                index -= 1
                jndex -= 1
                # print "Check", jndex, index, final
                
                x = 0
                while x < breadth and count < total:
                    count += 1
                    final[jndex][index] = count
                    index -= 1
                    x += 1
                length -= 1
                index += 1
                jndex -= 1
                # print "Check", jndex, index, matrix[jndex][index]
                
                x = 0
                while x < length and count < total:
                    count += 1
                    final[jndex][index] = count
                    jndex -= 1
                    x += 1
                breadth -= 1
                jndex += 1
                index += 1
                # print "Check", jndex, index, matrix[jndex][index]\
                
            return final
        else:
            return []
        
        
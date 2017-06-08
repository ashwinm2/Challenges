# Spiral Matrix
class Solution(object):
    def spiralOrder(self, matrix):
        final = []
        if matrix != []:
            length = len(matrix)
            breadth = len(matrix[0])
            count = 0
            total = length * breadth
            index = 0
            jndex = 0
            while count < total:
                x = 0
                while x < breadth and count < total:
                    final.append(matrix[jndex][index])
                    index = index + 1
                    count += 1
                    x += 1
                length -= 1
                jndex += 1
                index -= 1
                # print "Check", jndex, index, matrix[jndex][index]
                
                
                x = 0
                while x < length and count < total:
                    final.append(matrix[jndex][index])
                    jndex += 1
                    count += 1
                    x += 1
                breadth -= 1
                index -= 1
                jndex -= 1
                # print "Check", jndex, index, matrix[jndex][index]
                
                x = 0
                while x < breadth and count < total:
                    final.append(matrix[jndex][index])
                    index -= 1
                    count += 1
                    x += 1
                length -= 1
                index += 1
                jndex -= 1
                # print "Check", jndex, index, matrix[jndex][index]
                
                x = 0
                while x < length and count < total:
                    final.append(matrix[jndex][index])
                    jndex -= 1
                    count += 1
                    x += 1
                breadth -= 1
                jndex += 1
                index += 1
                # print "Check", jndex, index, matrix[jndex][index]
        return final
        
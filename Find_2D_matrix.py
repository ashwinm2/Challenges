# Find element in 2D matrix
class Solution(object):
    def check(self, temp, length, target):
        start = 0
        end = length - 1
        while start <= end:
            mid = (start + end)/ 2
            if target > temp[mid]:
                start = mid + 1
            elif target < temp[mid]:
                end = mid - 1
            else:
                return True
        return False
    
    def searchMatrix(self, matrix, target):
        if len(matrix) > 0 and len(matrix[0]) > 0:
            x_axis = len(matrix[0])
            y_axis = len(matrix)
            for y in range(y_axis):
                if target > matrix[y][0] and target < matrix[y][x_axis - 1]:
                    return self.check(matrix[y], x_axis, target)
                elif target == matrix[y][0]:
                    return True
                elif target == matrix[y][x_axis - 1]:
                    return True
            return False
        else:
            
            return False
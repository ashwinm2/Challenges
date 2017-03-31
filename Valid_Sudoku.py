# Valid Sudoku

def square(board):
    base = -3
    check = {}
    for each in range(0, 27):
        if each % 9 == 0:
            base += 3
        if each % 3 == 0:
            #print "Final", check
            #print "Proper"
            check = {}
            
        each = (each % 9)
        for iter in range(0, 3):
            val = iter + base
            if board[each][val] != '.':
                if board[each][val] not in check:
                    check[board[each][val]] = 0
                else:
                    #print "Check", check
                    #print each, iter + base,
                    return False
            #print board[each][val],
        #print ""
    return True

def bprint(board):
    for each in board:
        print each

class Solution(object):
    def col_check(self, board):
        check = {}
        for index in range(0,9):
            for each in board:
                if each[index] != '.': 
                    if each[index] not in check:
                        check[each[index]] = 0
                    else:
                        return False
            check = {}
        return True
        
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check = {}
        row = 0
        for item in board:
            temp = list(item)
            for ele in temp:
                if ele != '.':
                    if ele not in check:
                        check[ele] = ele
                    else:
                        return False
            board[row] = temp
            check = {}
            row += 1
        
        #bprint(board)
        if self.col_check(board):
            if square(board):
                return True
            else:
                return False
        else:
            return False

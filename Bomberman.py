# Bomberman
import copy
import sys

def compute(R, C, N, Matrix, total): 
    if N % 2 == 0 or N == 1:
        for i in range(0,R):
            for j in range(0,C): 
                if N == 1:
                    if Matrix[i][j] == -1:
                        sys.stdout.write('O')
                    else:
                        sys.stdout.write('.')
                elif N % 2 == 0:
                        sys.stdout.write('O')
            print ""
    else:
        temp = copy.deepcopy(Matrix)
        for i in range(0,R):
            for j in range(0,C):  
                if Matrix[i][j] == -1:
                    if i-1 >= 0:
                        temp[i-1][j] = -1
                        if (i-1,j) not in total:
                            total[(i-1,j)] = (i-1,j)
                    if j-1 >= 0:
                        temp[i][j-1] = -1
                        if (i,j-1) not in total:
                            total[(i,j-1)] = (i,j-1)
                    if i + 1 < R:
                        temp[i+1][j] = -1
                        if (i+1,j) not in total:
                            total[(i+1,j)] = (i+1,j)
                    if j + 1 < C:
                        temp[i][j+1] = -1
                        if (i,j+1) not in total:
                            total[(i,j+1)] = (i,j+1)
        M = (N / 2) + 1
        if M == 2:
            for i in range(0,R):
                for j in range(0,C):
                        if  (i, j) in total:
                            sys.stdout.write('.')
                        else:
                            sys.stdout.write('O')
                print ""
        else:
            benign = {}
            for key in total:
                i = key[0]
                j = key[1]
                if i-1 >= 0 and (i-1,j) not in total:
                    benign[(i,j)] = (i,j)        
                if j-1 >= 0 and (i,j-1) not in total:
                        benign[(i,j)] = (i,j)
                if i+1 < R and (i+1,j) not in total:
                        benign[(i,j)] = (i+1,j)
                if j+1 < C and (i,j+1) not in total:
                        benign[(i,j)] = (i,j+1)                        
            
            for i in range(0,R):
                for j in range(0,C):
                    if M % 2 == 0:
                        if (i,j) in total and (i,j) in benign:
                            sys.stdout.write('.')
                        elif (i,j) in total:
                            sys.stdout.write('.')
                        else:
                            sys.stdout.write('O')
                    else:
                        if (i,j) in total and (i,j) in benign:
                            sys.stdout.write('.')
                        elif (i,j) in total:
                            sys.stdout.write('O')
                        else:
                            sys.stdout.write('.')
                print ""
            
            
R,C,N = map(int,raw_input().split())
Matrix = []
total = {} 
for i in range(0,R):
    x = list(raw_input())
    temp = []
    for j in range(0, len(x)): 
        if x[j] == 'O':
            temp.append(-1)
            total[(i,j)] = (i,j)
        else:           
            temp.append(1)
    Matrix.append(temp)

compute(R, C, N, Matrix, total)
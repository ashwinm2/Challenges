def paint(i, j, target, current, matrix, n, m):
	if current == None:
		current = matrix[i][j]
	
	
	if i <= n - 1 and j <= m - 1 and i >=0 and j >= 0:
		if matrix[i][j] == current:
			matrix[i][j] = target
			print i, j
			if i - 1 >= 0:
				if matrix[i-1][j] == current:
					paint(i-1, j, target, current, matrix, n, m)
			if i + 1 <= n - 1:
				if matrix[i+1][j] == current:
					paint(i+1, j , target, current, matrix, n, m)
			if j - 1 >= 0:
				if matrix[i][j-1] == current:
					paint(i, j-1, target, current, matrix, n, m)
			if j + 1 <= m - 1: 
				if matrix[i][j+1] == current:
					paint(i, j+1, target, current, matrix, n, m)
		else:
			return 
	else:
		return 


n, m = map(int , raw_input().split())
matrix = [map(int, raw_input().split()) for j in range(n)]
paint(2, 2, 5, None, matrix, n, m)
for item in matrix:
	print item

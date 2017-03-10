# Coin arrangement or Steps problem - Square root
def cal(val):
	# Product of roots is less than or equal to 2 * val
	root = (-1 + (1+(8*val))**.5) / 2
	if root < 0:
		print (-1 - (1+(8*val))**.5) / 2
	else: 
		print int(root)

val = int(raw_input())
cal(val)
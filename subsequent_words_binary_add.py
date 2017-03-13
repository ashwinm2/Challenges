# Implementing the all subsequent words for given basestring
# Binary Addition

def compute(temp_lt, pointer):
	flag = 0
	check_lt = [1 for x in temp_lt]
	if temp_lt[pointer] == 0:
		temp_lt[pointer] = 1
	elif  temp_lt == check_lt:
		pass
	else:
		temp_lt[pointer] = 0
		temp_lt = compute(temp_lt, pointer - 1)
	return temp_lt


def iter(str):
	temp_lt = [0 for x in str]
	check_lt = [1 for x in str]
	while temp_lt != check_lt:
		temp_lt = compute(temp_lt, len(temp_lt) - 1)
		words = ''
		for x in range(0,len(temp_lt)):
			if temp_lt[x] == 1:
				words += str[x]
		print words
		

str = list(raw_input())
print str
iter(str)

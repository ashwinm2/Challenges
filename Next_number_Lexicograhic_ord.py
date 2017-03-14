#  Next sequence in the number in Lexicograhic order
def findNextbig(lt, val):
	lt = sorted(lt)
	for x in lt:
		if x > val:
			return lt.index(x)
	return None

def getNextno(value):
	value = [int(x) for x in value]
	last = value[-1]
	ptr = len(value) - 2 
	while ptr >= 0 and value[ptr] > last:
		last = value[ptr]
		ptr -= 1
	if ptr != -1:
		# print value[ptr] 
		pos = findNextbig(value[ptr+1:], value[ptr])
		pos = pos + ptr
		# print value[pos]
		value[ptr], value[pos] = value[pos], value[ptr]
		# print value
		value[ptr+1:] = sorted(value[ptr+1:])
	else:
		print 'Cannot do it.'
	print 'The value is ',value
	return value

def alptono(word):
	value = [ord(x) - 96 for x in word]
	value = getNextno(value)
	result = [chr(x - 1 + ord('a')) for x in value]
	print result

word = raw_input()
# alptono(word.lower())
getNextno(word)


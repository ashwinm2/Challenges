# Subsequence of a word in an iterative manner
def subq(str1, str2):
	if str2 == []:
		if len(str1) != 0:
			print ''.join(str1)
		return
	# 'Use it' part of the code where the an element is popped from str2 and pushed into str1
	#  Iteratively it reduces to the last value and gets printed
	# print 'Iteration ',str1, str2
	subq(str1 + [str2[0]],str2[1:])
	subq(str1,str2[1:])

str = list(raw_input())
subq([],str)
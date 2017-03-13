# Djikstra's Algorithm

def fetch():
	n, k = map(int,raw_input().strip().split(' '))
	full_dict = {}
	for j in range(0,k):
	    t = raw_input().split(' ')
	    # print t
	    if t[0] not in full_dict.keys():
	        temp = {t[1]:t[2]}
	        full_dict[t[0]] = temp
	    else:
	        temp = full_dict[t[0]]
	        if t[1] in temp.keys():
	        	if int(t[2]) < int(temp[t[1]]):
	        		temp[t[1]]= t[2]
	        else:
	        	temp[t[1]]= t[2]
	        full_dict[t[0]] = temp
	        
	    if t[1] not in full_dict.keys():
	        temp = {t[0]:t[2]}
	        full_dict[t[1]] = temp
	    else:
	        temp = full_dict[t[1]]
	        if t[0] in temp.keys():
	        	if int(t[2]) < int(temp[t[0]]):
	        		temp[t[0]] = t[2]
	        else:
	        	temp[t[0]] = t[2]
	        full_dict[t[1]] = temp
	node = raw_input()
	print full_dict
	return full_dict, node

def find_close(fdict, node, givenNode, givenVal):
	# print 'finding close ',givenNode, givenVal
	tot = int(givenVal)
	# while givenNode != node:
	tot += int(fdict[givenNode][1])
	# print fdict
		# givenNode = fdict[givenNode][0]
	return tot
	

def setNextNode(res, currNode):
	temp_d = {}
	for kndex in res.keys():
		if kndex == currNode:
			tlt = res[kndex]
			tlt[2] = 'true'
			res[kndex] = tlt 
		elif res[kndex][2] == 'false':
			temp_d[res[kndex][1]] = kndex
	
	small = [int(x) for x in temp_d.keys()]
	if small != []:
		currNode = temp_d[str(min(small))]
	else:
		currNode = None
	return res, currNode


def compute():
	final_dict, node = fetch() 
	res = {node:[node,'0','true']}
	currNode = node
	for x in final_dict.keys():
		edges = final_dict[currNode]
		for jndex in edges.keys():
			temp = edges[jndex]
			if jndex not in res.keys():
				evalNode = find_close(res, node, currNode, temp)
				print 'Adding the node ', jndex, currNode, temp, evalNode				
				res[jndex] = [currNode,str(evalNode),'false']
			else:
				# print 'The current set is ', currNode, temp
				# print 'The actual set is ', res[jndex][0], res[jndex][1]
				currVal = find_close(res, node, res[jndex][0], res[jndex][1])
				checkVal = find_close(res, node, currNode, temp)
				print 'The actual set is ', currVal, checkVal
				if checkVal < currVal:
					res[jndex] = [currNode, str(checkVal),'false']
		
		print res
		res, currNode = setNextNode(res, currNode)
		print res, currNode
	return res
		
section = int(raw_input())
for i in range(0, section):
	result = compute()
	lt = result.keys()
	lt = sorted(lt)
	for x in lt:
		if result[x][1] != '0':
			print result[x][1],
	
	
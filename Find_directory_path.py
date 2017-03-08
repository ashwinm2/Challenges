# Find the directory path
full = raw_input()
stv = 0
stlt = []
current = 0
counter = 0
maxv = 0
i = 0
while i < len(full):
  if full[i] == '\\' and full[i+1] == 'n':
    i = i + 2
    temp = 0
    tempmax = 0
    while full[i] == '\\' and full[i+1] == 't':
      temp += 1
      i = i + 2
    print "current is ", current
    print "String until now", full[:i]
    
    print "Current len ", current
    tempmax = current + stv
    print "Current max", tempmax
    print "Old max", maxv
    if maxv < tempmax:
      maxv = tempmax
    print "Changed max", maxv
    print "Current stack and Value", stlt, stv
    current = current + 1
    if counter < temp:
      stlt.append(current)
      stv += current
      counter = temp
      print "Changed stack and Value", stlt, stv  
    elif counter > temp:
      while counter != temp:
        counter -= 1
        val = stlt.pop()
        stv -= val 
      print "Changed stack and Value", stlt, stv  
    else:
      print "No change"
    
    current = 0
  else:
    print "current = ",current, "char is ", full[i]
    current = current + 1
    i = i + 1
  
  

print "current is ", current
print "String until now", full[:i]

print "Current len ", current
tempmax = current + stv
print "Current max", tempmax
print "Old max", maxv
if maxv < tempmax:
  maxv = tempmax
print "Changed max", maxv


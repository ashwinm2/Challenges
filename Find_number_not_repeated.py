# Finding the number that is not repeated in the given list of numbers
# glist = map(int, raw_input().strip(' ').split())
# temp = None
# for i in glist:
#   if temp == None:
#     temp = i
#   else:
#     temp = temp ^ i
# print temp


# Extension of the above problem to find 2 numbers that are repeated in the given list of numbers
glist = map(int, raw_input().strip(' ').split())
temp = None
for i in glist:
  if temp == None:
    temp = i
  else:
    temp = temp ^ i

a = 1
i = 0
while (temp & (a << i)) != (a << i):
  i = i + 1

llist = []
rlist = []
for j in glist:
  if j & a << i == a << i:
    llist.append(j)
  else:
    rlist.append(j)

ltemp = None
for index in llist:
  if ltemp == None:
    ltemp = index
  else:
    ltemp = ltemp ^ index
print ltemp, # "{0:b}".format(ltemp)

rtemp = None
for index in rlist:
  if rtemp == None:
    rtemp = index
  else:
    rtemp = rtemp ^ index
print rtemp, # "{0:b}".format(rtemp)
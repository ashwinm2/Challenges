# Bit Manipulation to get next largest and smallest
def rev(temp):
  final = 0
  while temp:
    final = (final << 1) | (temp & 1)
    temp = temp >> 1
  return final

bin = int(raw_input(), 2)
sam = bin
print "{0:b}".format(bin)

flag = 0
sam = bin
a = 1
i = 0
while flag != 1:
  if bin & (a << i) == (a << i) and bin & (a << (i + 1)) != (a << (i + 1)):
    bin = bin | (a << (i + 1))
    bin = bin & ~(a << i)
    # Reversing the remaining part
    if i > 0:
      temp = int('1'* i, 16)
      rem = bin & temp
      bin = bin & ~(temp)
      bin = bin | rev(rem)
    flag = 1
  else:
    i = i + 1
    
print "{0:b}".format(bin)

flag = 0
i = 0
while flag != 1:
  if sam & (a << i) != (a << i) and sam & (a << (i + 1)) == (a << (i + 1)):
    sam = sam | (a << i)
    sam = sam & ~(a << (i + 1))
    # Reversing the remaining part
    if i > 0:
      temp = int('1'* i, 16)
      rem = sam & temp
      sam = sam & ~(temp)
      sam = sam | rev(rem)
    print "{0:b}".format(sam)
    flag = 1
  else:
    i = i + 1





# Double to bit conversion
def extract(val):
  val = val * 2
  temp = int(val)
  val = val % 1
  return temp, val 

def compute(val):
  final = []
  while val != 0.0: 
    if len(final) < 31:
      temp, val = extract(val)
      final.append(str(temp))
    else:
      return 'Error'
  return '0.' + ''.join(final)
  
val = float(raw_input())
print compute(val)

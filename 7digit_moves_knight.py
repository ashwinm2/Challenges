# 7 digit numbers that start with 0 and moves similar to a Knight
from copy import deepcopy

class Calc(object):
  def __init__(self):
    self.count = 0
  
  def f(self, x):
    return {
      0:[4, 6],
      1:[6, 8],
      2:[7, 9],
      3:[4, 8],
      4:[0, 3, 9],
      6:[0, 1, 7],
      7:[2, 6],
      8:[1, 3],
      9:[2, 4]
    }[x]
  
  def compute(self, cur, last, l):
    if l < 7:
      temp = self.f(last)
      for each in temp:
        stack = deepcopy(cur)
        stack.append(each)
        self.compute(stack, each, l+1)
    else:
      print cur
      self.count += 1
    

obj = Calc()
obj.compute([0], 0, 1)
print obj.count


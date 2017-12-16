
# Puzzle 16: Permutation Promenade
# http://adventofcode.com/2017/day/16

class Advent16:
  def __init__(self, steps = None, progs = 16):
    self.steps = steps if steps != None else self.loadSampleData()
    self.programs = map(lambda x: chr(ord('a')+x), range(progs))

  def loadSampleData(self):
    raw = open("./data/advent16.txt").read()
    result = []
    for line in raw.split("\n"):
      result += line.split(",")
    return result

  def dance(self):
    for ds in self.steps:
      self.step(ds)
    return ''.join(self.programs)

  def step(self, ds):
    p0 = ds[0]
    c0 = ds[1:].split('/')
    p1 = '' if len(c0) < 1 else c0[0]
    p2 = '' if len(c0) < 2 else c0[1]

    # 'p' = Swap values by program name, convert to an equivalent 'x'
    if p0 == 'p':
      p0 = 'x'
      p1 = self.programs.index(p1)
      p2 = self.programs.index(p2)

    # 's' = Spin, use list slicing
    if p0 == 's':
      self.programs = self.programs[-int(p1):] + self.programs[:-int(p1)]

    # 'x' = Swap values by index
    if p0 == 'x':
      temp = self.programs[int(p1)]
      self.programs[int(p1)] = self.programs[int(p2)]
      self.programs[int(p2)] = temp

  def getPermutationResult(self):
    return self.dance()

  def getPermutationResultExtra(self):
    # Brute force isn't viable at 1 billion iterations!
    # Memoize the result and skip repeating cycles
    memo = []
    key = ''.join(self.programs)
    while not key in memo:
      memo += [key]
      key = self.dance()

    for n in range(1000000000 % len(memo)):
      key = self.dance()

    return key


if __name__=='__main__':
  print(Advent16().getPermutationResult())
  print(Advent16().getPermutationResultExtra())


# Puzzle 6: Memory Reallocation
# http://adventofcode.com/2017/day/6

class Advent06:
  def __init__(self, memory = None):
    self.memory = memory
    self.prev_states = {}
    if not memory:
      self.memory = self.loadSampleData()

  def loadSampleData(self):
    raw = open("./data/advent06.txt").read()
    return [int(line) for line in raw.split("\n")]

  def findLargestBank(self):
    max_value = 0
    max_index = 0
    for i in range(0,len(self.memory)):
      if self.memory[i] > max_value:
        max_value = self.memory[i]
        max_index = i
    return max_index

  def reallocLargestBank(self):
    mx = self.findLargestBank()
    mx_val = self.memory[mx]
    self.memory[mx] = 0
    for i in range(mx+1,mx+1+mx_val):
      self.memory[i % len(self.memory)] += 1
    return mx_val

  def storeState(self):
    if not self.prev_states.has_key(self.stateKey()):
      self.prev_states[self.stateKey()] = self.reallocCount()
      return True
    return False

  def reallocCount(self):
    return len(self.prev_states.keys())

  def stateKeyLastSeen(self):
    return self.prev_states[self.stateKey()]

  def stateKey(self):
    return tuple(self.memory)

  def getReallocResult(self):
    while self.storeState():
      self.reallocLargestBank()
    return self.reallocCount()

  def getReallocResultExtra(self):
    while self.storeState():
      self.reallocLargestBank()
    return self.reallocCount() - self.stateKeyLastSeen()


if __name__=='__main__':
  print(Advent06().getReallocResult())
  print(Advent06().getReallocResultExtra())


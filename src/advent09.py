
# Puzzle 9: Stream Processing
# http://adventofcode.com/2017/day/9

class Advent09:
  def __init__(self, stream = None):
    self.stream = stream or self.loadSampleData()

  def loadSampleData(self):
    return open("./data/advent09.txt").read()

  def countGroups(self):
    (a,b) = self.processStream()
    return a

  def countGarbage(self):
    (a,b) = self.processStream()
    return b

  def processStream(self):
    i = 0
    garbage = False
    groupStack = 0
    groupCount = 0
    garbageCount = 0

    while i < len(self.stream):
      c = self.stream[i]
      if garbage:
        if c == '>':
          garbage = False
        elif c == '!':
          i += 1
        else:
          garbageCount += 1
      else:
        if c == '<':
          garbage = True
        elif c == '{':
          groupStack += 1
        elif c == '}' and groupStack > 0:
          groupCount += groupStack
          groupStack -= 1
      i += 1
    return (groupCount,garbageCount)


if __name__=='__main__':
  print(Advent09().getStreamResult())
  print(Advent09().getStreamResultExtra())


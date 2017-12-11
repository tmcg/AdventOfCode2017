
# Puzzle 10: Knot Hash
# http://adventofcode.com/2017/day/10

from operator import xor

class Advent10:
  def __init__(self, ring = None):
    self.ring = ring if ring != None else range(256)
    self.inputs = []
    self.pos = 0
    self.skip = 0

  def initInputs(self, inputs = None, convertToAscii = False):
    if convertToAscii:
      self.inputs = inputs if inputs != None else self.loadSampleDataAsString()
      self.inputs = [ord(x) for x in self.inputs] + [17,31,73,47,23]
    else:
      self.inputs = inputs if inputs != None else self.loadSampleDataAsList()

  def loadSampleDataAsString(self):
    return open("./data/advent10.txt").read()

  def loadSampleDataAsList(self):
    return [int(x) for x in self.loadSampleDataAsString().split(",")]

  def performKnotHash(self, rounds = 1):
    for y in range(rounds):
      for x in self.inputs:
        temp = self.ring[self.pos:] + self.ring[:self.pos]
        temp = temp[:x][::-1] + temp[x:]
        self.ring = temp[-self.pos:] + temp[:-self.pos]
        self.pos = (self.pos + x + self.skip) % len(self.ring)
        self.skip += 1

  def denseHash(self, blockSize = 16):
    hash = ''
    for b in range(len(self.ring)/blockSize):
      temp = self.ring[b*blockSize:b*blockSize+blockSize]
      hash += '{:02x}'.format(reduce(xor, temp))
    return hash

  def getKnotHashResult(self):
    self.performKnotHash()
    return self.ring[0]*self.ring[1]

  def getKnotHashResultExtra(self):
    self.performKnotHash(64)
    return self.denseHash()


if __name__=='__main__':
  t = Advent10()
  t.initInputs()
  print(t.getKnotHashResult())

  t = Advent10()
  t.initInputs(None,True)
  print(t.getKnotHashResultExtra())


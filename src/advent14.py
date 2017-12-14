
# Puzzle 14: Knot Hash
# http://adventofcode.com/2017/day/14

from operator import xor

class Advent14:
  def __init__(self):
    self.debug = False

  def getKnotHash(self, s):
    ring = range(256)
    inputs = [ord(x) for x in s] + [17,31,73,47,23]
    pos = 0
    skip = 0
    rounds = 64

    for y in range(rounds):
      for x in inputs:
        temp = ring[pos:] + ring[:pos]
        temp = temp[:x][::-1] + temp[x:]
        ring = temp[-pos:] + temp[:-pos]
        pos = (pos + x + skip) % len(ring)
        skip += 1

    return self.denseHash(ring)

  def denseHash(self, ring, blockSize = 16):
    hash = ''
    for b in range(len(ring)/blockSize):
      temp = ring[b*blockSize:b*blockSize+blockSize]
      hash += '{:02x}'.format(reduce(xor, temp))
    return hash

  def getBitArray(self, hash):
    bitArray = []
    for hd in [d.lower() for d in hash]:
      bitArray += [int(c) for c in '{0:0>4b}'.format(int(hd,16))]
    return bitArray

  def generateHashGrid(self, key):
    grid = range(0,128)
    for rowId in grid:
      rowKey = key + '-' + str(rowId)
      grid[rowId] = self.getBitArray(self.getKnotHash(rowKey))
    return grid

  def debugHashGrid(self, grid):
    print("==============")
    for rowId in range(0,len(grid)):
      print(grid[rowId])

  def getDefragResult(self, key):
    grid = self.generateHashGrid(key)
    return sum([sum(row) for row in grid])

  def exploreRegion(self, grid, x, y, xMax, yMax, nextGroup):
    if y < 0 or y >= yMax or x < 0 or x >= xMax:
      return 0 # out of bounds

    if grid[y][x] < 0:
      # square we haven't seen before
      grid[y][x] = nextGroup
      # recursively find all adjacent squares
      self.exploreRegion(grid, x, y-1, xMax, yMax, nextGroup) # search up
      self.exploreRegion(grid, x, y+1, xMax, yMax, nextGroup) # search down
      self.exploreRegion(grid, x-1, y, xMax, yMax, nextGroup) # search left
      self.exploreRegion(grid, x+1, y, xMax, yMax, nextGroup) # search right
      return 1
    return 0

  def findContigRegions(self, grid):
    # The grid is passed into here as: no square = 0, square = 1
    # Convert it for easier counting: no square = 0, square = -1
    for rowId in range(0,len(grid)):
      grid[rowId] = [-1*n for n in grid[rowId]]

    nextGroup = 1
    for ty in range(0,len(grid)):
      for tx in range(0,len(grid[ty])):
        increment = self.exploreRegion(grid, tx, ty, len(grid[ty]), len(grid), nextGroup)
        nextGroup += increment
        if self.debug and increment > 0:
          # a group was found, debug print
          self.debugHashGrid(grid)

    return nextGroup - 1

  def getDefragResultExtra(self, key):
    grid = self.generateHashGrid(key)
    return self.findContigRegions(grid)

if __name__=='__main__':
  print(Advent14().getDefragResult('uugsqrei'))
  print(Advent14().getDefragResultExtra('uugsqrei'))

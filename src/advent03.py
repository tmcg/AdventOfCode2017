
# Puzzle 3: Find the path to the access port
# http://adventofcode.com/2017/day/3

import math

class Advent03:
  def start(self):
    print("== Advent Day 3")
    print(self.getSpiralResult(265149))
    print(self.getSpiralResultExtra(265149))

  def getRingSize(self, n):
    if n == 0:
      return 0
    return self.getRingSize(n-1)+8

  def getRingStart(self, n):
    if n == 1:
      return 2
    return self.getRingStart(n-1)+self.getRingSize(n-1)

  def getRingNumber(self, n):
    if n == 1:
      return 0

    for ring_number in range(1,10000):
      ring_start = self.getRingStart(ring_number)
      ring_size = self.getRingSize(ring_number)
      if n >= ring_start and n < (ring_start + ring_size):
        return ring_number

    raise OverflowError('n is too large!')

  def getSpiralResult(self, n):
    ring_number = self.getRingNumber(n)
    ring_start = self.getRingStart(ring_number)
    ring_size = self.getRingSize(ring_number)
    edge_size = ring_size/4

    edge_starts = [ring_start+(edge_size*x) for x in range(0,4)]
    edge_start = [x for x in edge_starts if n >= x and n < x + edge_size]
    edge_center = edge_start[0] - 1 + math.floor(edge_size / 2)
    return ring_number + int(max(edge_center,n)) - int(min(edge_center,n))

  def getSpiralResultExtra(self, n):
    width, height = 20, 20
    x, y = 10, 10
    heading = 0  # 0,1,2,3 = right,up,left,down
    grid = [[0 for xx in range(width)] for yy in range(height)]

    sum_above = lambda g,x,y: g[y-1][x-1]+g[y-1][x]+g[y-1][x+1]
    sum_below = lambda g,x,y: g[y+1][x-1]+g[y+1][x]+g[y+1][x+1]
    sum_adjacent = lambda g,x,y: sum_above(g,x,y)+sum_below(g,x,y)+g[y][x-1]+g[y][x+1]

    grid[y][x] = 1
    turn_left = lambda z: (z + 1) % 4

    for i in range(0,100):
      if heading == 0:
        x += 1
        ty,tx = y-1,x # check up
      elif heading == 1:
        y -= 1
        ty,tx = y,x-1 # check left
      elif heading == 2:
        x -= 1
        ty,tx = y+1,x # check down
      else:
        y += 1
        ty,tx = y,x+1 # check right

      grid_value = sum_adjacent(grid,x,y)
      if grid_value > n:
        return grid_value
      grid[y][x] = grid_value
      if grid[ty][tx] == 0:
        heading = turn_left(heading)

    return 0


if __name__=='__main__':
  Advent03().start()
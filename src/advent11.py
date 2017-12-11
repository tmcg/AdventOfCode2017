
# Puzzle 11: Hex Ed
# http://adventofcode.com/2017/day/11

class Advent11:
  def __init__(self, steps = None):
    self.steps = steps if steps != None else self.loadSampleData()

  def loadSampleData(self):
    raw = open("./data/advent11.txt").read()
    return [step for step in raw.split(",")]

  # Hex Grid Definition (x,y,z)
  # https://www.redblobgames.com/grids/hexagons/
  # Co-ordinates invariant: x + y + z = 0
  # =        ==        ==
  #   \    /    \    /    \
  #     == -1,2,-1== 1,1,-2 ==
  #   /    \    /    \    /
  # =        == 0,1,-1 == 2,0,-2
  #   \    /    \    /    \
  #     == -1,1,0 == 1,0,-1 ==
  #   /    \    /    \    /
  # =        == 0,0,0  ==
  #   \    /    \    /    \
  #     ==        ==        ==

  # Moving on the hex grid affects two axes at a time.
  # North <=> South affects Y and Z
  # N'East <=> S'West affects X and Z
  # N'West <=> S'East affects X and Y
  #
  #     +Y    / -Z
  #       \  /
  #  X ____\/___ +X
  #       / \
  #      /   \
  #    +Z     -Y

  def getHexPath(self):
    # The distance from origin (0,0,0) to any
    # arbitrary point (x,y,z) is defined by the formula:
    #   d = max(abs(x),abs(y),abs(z))
    adds = {
      'n': (0,1,-1), 's': (0,-1,1),
      'ne': (1,0,-1), 'se': (1,-1,0),
      'sw': (-1,0,1), 'nw': (-1,1,0)
    }
    max_dist = 0
    max_ever = 0
    x = 0
    y = 0
    z = 0
    for step in self.steps:
      x += adds[step][0]
      y += adds[step][1]
      z += adds[step][2]
      max_dist = max(abs(x),abs(y),abs(z))
      if max_dist > max_ever:
        max_ever = max_dist

    return (max_dist, max_ever)

  def getHexPathResult(self):
    (max_dist,max_ever) = self.getHexPath()
    return max_dist

  def getHexPathResultExtra(self):
    (max_dist,max_ever) = self.getHexPath()
    return max_ever


if __name__=='__main__':
  print(Advent11().getHexPathResult())
  print(Advent11().getHexPathResultExtra())


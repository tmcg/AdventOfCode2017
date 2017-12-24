
# Puzzle 21: Fractal Art
# http://adventofcode.com/2017/day/21

class Artwork:
  def __init__(self, s = '../..'):
    self.s = s

  def flipv(self):
    self.s = self._flip(self.s,True)
    return self

  def fliph(self):
    self.s = self._flip(self.s,False)
    return self

  def rotate(self, turns = 1):
    t = turns % 4
    for n in range(t):
      self.s = self._rotate(self.s)
    return self

  def _flip(self, s, vertical = True):
    parts = s.split('/')
    if vertical:
      parts.reverse()
    else:
      for n in range(len(parts)):
        parts[n] = parts[n][::-1]
    return '/'.join(parts)

  def _rotate(self, s):
    parts = s.split('/')
    size = len(parts[0])
    if size == 2:
      p0 = parts[1][0] + parts[0][0]
      p1 = parts[1][1] + parts[0][1]
      parts = [p0,p1]
    elif size == 3:
      p0 = parts[2][0] + parts[1][0] + parts[0][0]
      p1 = parts[2][1] + parts[1][1] + parts[0][1]
      p2 = parts[2][2] + parts[1][2] + parts[0][2]
      parts = [p0,p1,p2]
    else:
      raise("Invalid size! ({0})".format(size))

    return '/'.join(parts)

class Advent21:
  def __init__(self, rules = None):
    rules = rules if rules != None else self.loadSampleData()
    self.rules = self.decodeRules(rules)
    # self.grid is a 2D array of artworks in string form.
    # Don't parse the artworks further into a nested 2D arrays
    # until the grid is transformed as it hinders match lookups
    self.grid = [['.#./..#/###']]
    self.pixels = 0

  def loadSampleData(self):
    raw = open("./data/advent21.txt").read()
    return [line for line in raw.split("\n")]

  def decodeRules(self, rules):
    rdict = {}
    for rule in [r.split(' => ') for r in rules]:
      ra0 = Artwork(rule[0])
      ra1 = Artwork(ra0.s).rotate(1)
      ra2 = Artwork(ra1.s).rotate(1)
      ra3 = Artwork(ra2.s).rotate(1)
      # Generate any missing rules to optimise lookups
      rslist = [
        ra0.s, Artwork(ra0.s).flipv().s, Artwork(ra0.s).fliph().s,
        ra1.s, Artwork(ra1.s).flipv().s, Artwork(ra1.s).fliph().s,
        ra2.s, Artwork(ra2.s).flipv().s, Artwork(ra2.s).fliph().s
      ]

      for rs in rslist:
        rval = rdict.get(rs,'')
        if rval != '' and rval != rule[1]:
          raise('Rule conflict!')
        rdict[rs] = rule[1]

    return rdict

  def transform(self):
    # Apply a transform rule to each artwork in the grid
    for y in range(len(self.grid)):
      for x in range(len(self.grid[y])):
        self.grid[y][x] = self.rules[self.grid[y][x]]

    # Then, concatenate the entire grid into a string
    # and rebuild it based on the new art block size

    # csize = the size of artworks after applying rules (ie. 3x3 or 4x4)
    csize = self.grid[0][0].index('/')
    # width = total width of the flattened pixel square (csize * no of works)
    width = csize * len(self.grid[0])
    # newsize = the new size of broken up artworks
    newsize = 2 if width % 2 == 0 else 3
    # reps = the number of artworks on a single row/column of the new grid
    newnum = width / newsize

    # flatten all artworks into a single array
    flat = ''
    for row in self.grid:
      for n in range(csize):
        flat += ''.join(s.split('/')[n] for s in row)

    # construct a new artwork grid based on the new size
    newgrid = []
    for rr in range(newnum):
      rrs = rr * newsize * width
      newrow = []
      for rc in range(newnum):
        rcs = rc * newsize + rrs
        ss = flat[rcs:rcs+newsize]
        rcs += width
        ss += '/' + flat[rcs:rcs+newsize]
        if newsize == 3:
          rcs += width
          ss += '/' + flat[rcs:rcs+newsize]
        newrow.append(ss)

      newgrid.append(newrow)

    # the flat array is convenient to count pixels as well
    self.pixels = len([x for x in flat if x == '#'])
    self.grid = newgrid

  def getFractalResult(self):
    for n in range(5):
      self.transform()
    return self.pixels

  def getFractalResultExtra(self):
    for n in range(18):
      self.transform()
    return self.pixels


if __name__=='__main__':
  print(Advent21().getFractalResult())
  print(Advent21().getFractalResultExtra())

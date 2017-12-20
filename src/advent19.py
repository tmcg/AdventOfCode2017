
# Puzzle 19: A Series of Tubes
# http://adventofcode.com/2017/day/19

class Advent19:
  def __init__(self, board = None):
    rows = board if board != None else self.loadSampleData()
    self.board = self.decodeRows(rows)
    self.pos = (self.board[0].index('|'),0)
    self.pointing = 2  # N=0, E=1, S=2, W=3
    self.letters = '' # Collected letters
    self.steps = 1 # Step count, 1 = starting position

  def loadSampleData(self):
    raw = open("./data/advent19.txt").read()
    return [line for line in raw.split("\n")]

  def decodeRows(self, rows):
    if rows == []:
      rows = ['']
    # pad the input to the longest line
    maxlen = max([len(row) for row in rows])
    return [[c for c in row.ljust(maxlen)] for row in rows]

  def lookLeft(self):
    return (self.pointing + 3) % 4

  def lookRight(self):
    return (self.pointing + 1) % 4

  def nextPos(self, pointing):
    nx = self.pos[0] + (1 if pointing == 1 else 0) + (-1 if pointing == 3 else 0)
    ny = self.pos[1] + (1 if pointing == 2 else 0) + (-1 if pointing == 0 else 0)
    return (nx,ny)

  def nextChar(self, pointing):
    (nx,ny) = self.nextPos(pointing)
    if nx < 0 or ny < 0 or nx >= len(self.board[0]) or ny >= len(self.board):
      return ' ' # scrolled off the board!
    return self.board[ny][nx]

  def currChar(self):
    return self.board[self.pos[1]][self.pos[0]]

  def forward(self):
    nch = self.nextChar(self.pointing)
    if nch != ' ':
      if nch.isalpha():
        self.letters += nch
      self.pos = self.nextPos(self.pointing)
      self.steps += 1
      return True
    return False

  def step(self):
    if self.currChar() == '+':
      # turn left or right
      leftTurn = self.lookLeft()
      if self.nextChar(leftTurn) != ' ':
        self.pointing = leftTurn
        return self.forward()

      rightTurn = self.lookRight()
      if self.nextChar(rightTurn) != ' ':
        self.pointing = rightTurn
        return self.forward()

      return False

    return self.forward()

  def getTubesResult(self):
    while self.step():
      pass
    return self.letters

  def getTubesResultExtra(self):
    while self.step():
      pass
    return self.steps

if __name__=='__main__':
  print(Advent19().getTubesResult())
  print(Advent19().getTubesResultExtra())

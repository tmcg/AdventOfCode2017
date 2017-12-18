
# Puzzle 17: Spinlock
# http://adventofcode.com/2017/day/17

class Advent17:
  def __init__(self):
    self.pos = 0
    self.next = 1
    self.buffer = [0]

  def spin(self, length, useBuffer = True):
    p = (length + self.pos) % self.next
    if useBuffer:
      # Calculate the buffer only if required.
      # It's needed for part 1, but slows down part 2 too much
      self.buffer = self.buffer[:p+1] + [self.next] + self.buffer[p+1:]
    self.pos = p + 1
    self.next += 1
    # emit the value if it was added after zero
    return self.next - 1 if p == 0 else 0

  def getSpinlockResult(self, reps, length):
    for r in range(reps):
      self.spin(length)

    return self.buffer[(self.pos + 1) % len(self.buffer)]

  def getSpinlockResultExtra(self, reps, length):
    afterZero = 0
    for f in range(reps):
      val = self.spin(length, False)
      if val != 0:
        # keep track of the last value inserted after zero
        afterZero = val
    return afterZero


if __name__=='__main__':
  print(Advent17().getSpinlockResult(2017,355))
  print(Advent17().getSpinlockResultExtra(50000000,355))

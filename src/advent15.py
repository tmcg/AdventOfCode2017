
# Puzzle 15: Dueling Generators
# http://adventofcode.com/2017/day/15

from operator import xor

class Generator:
  def __init__(self, start, factor, mod = 1):
    self.factor = factor
    self.start = start
    self.mod = mod

  def get(self, length):
    val = self.start
    curr = 0
    while curr < length:
      val = (val * self.factor) % 2147483647
      if val % self.mod == 0:
        curr += 1
        yield val


class Advent15:
  def __init__(self, startA, startB, modA = 1, modB = 1):
    self.a = Generator(startA, 16807, modA)
    self.b = Generator(startB, 48271, modB)

  def getDuelResult(self, length):
    ga = self.a.get(length)
    gb = self.b.get(length)

    try:
      matches = 0
      while True:
        an = ga.next()
        bn = gb.next()
        if an & 0xffff == bn & 0xffff:
          matches += 1
    except StopIteration:
      pass

    return matches


if __name__=='__main__':
  print(Advent15(277,349).getDuelResult(40000000))
  print(Advent15(277,349,4,8).getDuelResult(5000000))

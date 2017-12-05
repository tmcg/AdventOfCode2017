
# Puzzle 4: High-Entropy Passphrases
# http://adventofcode.com/2017/day/4

class Advent04:
  def start(self):
    d = self.loadSampleData()
    print("== Advent Day 4")
    print(self.getPassphraseResult(d))
    print(self.getPassphraseResultExtra(d))

  def loadSampleData(self):
    return open("./data/advent04.txt").read()

  def hasDuplicates(self, s):
    ls = s.split(' ')
    counts = {i:ls.count(i) for i in ls}
    for key in counts.iterkeys():
      if counts[key] >= 2:
        return True

    return False

  def hasAnagramDuplicates(self, s):
    ls = s.split(' ')
    ls = [''.join(sorted(i)) for i in ls]
    counts = {i:ls.count(i) for i in ls}
    for key in counts.iterkeys():
      if counts[key] >= 2:
        return True

    return False

  def getPassphraseResult(self, s):
    return len([0 for line in s.split("\n") if not self.hasDuplicates(line)])

  def getPassphraseResultExtra(self, s):
    return len([0 for line in s.split("\n") if not self.hasAnagramDuplicates(line)])


if __name__=='__main__':
  Advent04().start()

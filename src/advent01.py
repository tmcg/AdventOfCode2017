
# Puzzle 1: Find the sum of matching numbers
# http://adventofcode.com/2017/day/1

class Advent01:
  def start(self):
    d = self.loadSampleData()
    print("== Advent Day 1")
    print(self.getInverseCaptchaResult(d))
    print(self.getInverseCaptchaResultExtra(d))

  def loadSampleData(self):
    return open("./data/advent01.txt").read()

  def getInverseCaptchaResult(self, s):
    result = 0
    ls = [int(s[-1:])] + [int(n) for n in s]
    for i in range(0,len(ls)-1):
      if ls[i] == ls[i+1]:
        result += ls[i]
    return result

  def getInverseCaptchaResultExtra(self, s):
    result = 0
    ls = [int(n) for n in s]
    hlen = len(ls)/2
    for i in range(0,hlen):
      if ls[i] == ls[i+hlen]:
        result += ls[i]*2
    return result


if __name__=='__main__':
  Advent01().start()

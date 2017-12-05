
# Puzzle 2: Find the spreadsheet checksum
# http://adventofcode.com/2017/day/2

class Advent02:
  def start(self):
    d = self.loadSampleData()
    print("== Advent Day 2")
    print(self.getCheckSumResult(d))
    print(self.getCheckSumResultExtra(d))

  def loadSampleData(self):
    return open("./data/advent02.txt").read()

  def getCheckSumResult(self, s):
    sheet = [[int(x) for x in line.split()] for line in s.split("\n")]
    return sum([max(line) - min(line) for line in sheet])

  def getCheckSumResultExtra(self, s):
    result = 0
    sheet = [[int(x) for x in line.split()] for line in s.split("\n")]
    for line in sheet:
      result_list = []
      for i in range(0,len(line)):
        result_list += [x/line[i] for x in line[i+1:] if x % line[i] == 0]
        result_list += [line[i]/x for x in line[i+1:] if line[i] % x == 0]
      result += result_list[0]
    return result


if __name__=='__main__':
  Advent02().start()

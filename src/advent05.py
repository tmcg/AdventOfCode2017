
# Puzzle 5: A Maze of Twisty Trampolines, All Alike
# http://adventofcode.com/2017/day/5

class Advent05:
  def start(self):
    d = self.loadSampleData()
    print("== Advent Day 5")
    print(self.getTrampolineResult(d))
    print(self.getTrampolineResultExtra(d))

  def loadSampleData(self):
    raw = open("./data/advent05.txt").read()
    return [int(line) for line in raw.split("\n")]

  def getTrampolineResult(self, memory):
    jump_count = 0
    ip = 0

    while True:
      if ip < 0 or ip >= len(memory):
        return jump_count

      jump_dist = memory[ip]
      memory[ip] += 1
      jump_count += 1
      ip += jump_dist

  def getTrampolineResultExtra(self, memory):
    jump_count = 0
    ip = 0

    while True:
      if ip < 0 or ip >= len(memory):
        return jump_count

      jump_dist = memory[ip]
      memory[ip] += -1 if jump_dist >= 3 else 1
      jump_count += 1
      ip += jump_dist


if __name__=='__main__':
  Advent05().start()

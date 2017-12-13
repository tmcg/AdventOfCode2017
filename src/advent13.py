
# Puzzle 13: Packet Scanners
# http://adventofcode.com/2017/day/13

class Advent13:
  def __init__(self, firewall = None):
    self.firewall = firewall if firewall != None else self.loadSampleData()

  def loadSampleData(self):
    raw = open("./data/advent13.txt").read()
    d = {}
    for k,v in [line.split(':') for line in raw.split("\n")]:
      d[int(k)] = int(v)
    return d

  def getRangeAtDepth(self, depth):
    return self.firewall.get(depth,0)

  def isScannerAtTop(self, depth, time):
    rg = self.getRangeAtDepth(depth)
    if rg > 1:
      return 0 == time % ((2*rg) - 2)
    return rg == 1

  def getFirewallResult(self, delay = 0):
    severity = 0
    for depth in range(0,max(self.firewall.keys()) + 1):
      time = depth + delay
      if self.isScannerAtTop(depth, time):
        rg = self.getRangeAtDepth(depth)
        severity += rg * depth
    return severity

  def getFirewallResultExtra(self):
    delay = 0
    while True:
      caught = False
      for depth in range(0,max(self.firewall.keys()) + 1):
        time = depth + delay
        if self.isScannerAtTop(depth, time):
          caught = True
          break

      if not caught:
        return delay
      delay += 1


if __name__=='__main__':
  print(Advent13().getFirewallResult())
  print(Advent13().getFirewallResultExtra())


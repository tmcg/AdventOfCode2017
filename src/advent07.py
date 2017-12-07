
# Puzzle 7: Recursive Circus
# http://adventofcode.com/2017/day/7

class Program:
  def __init__(self,name,weight,childNames):
    self.name = name
    self.weight = weight
    self.childNames = childNames
    self.parent = None
    self.children = []

class Advent07:
  def __init__(self, tower_programs = None):
    programs = tower_programs or self.loadSampleData()
    self.tower = self.assembleTower([self.parseTowerProgram(p) for p in programs])

  def loadSampleData(self):
    raw = open("./data/advent07.txt").read()
    return [line for line in raw.split("\n")]

  def assembleTower(self, all_programs):
    if len(all_programs) == 0:
      return None

    for program in all_programs:
      parent = [p for p in all_programs if program.name in p.childNames]
      if len(parent) > 0:
        program.parent = parent[0]
        parent[0].children.append(program)

    # Find the root, it's the only one without a parent
    return [p for p in all_programs if p.parent is None][0]

  def unbalancedAdjustment(self, program):
    # If a program has < 3 children then ambiguity can't be resolved
    if len(program.children) >= 3:
      childWeights = [self.findTreeWeight(child) for child in program.children]
      childFrequency = {k:childWeights.count(k) for k in childWeights}
      unbalancedWeight = [u for u in childFrequency if childFrequency[u] == 1]
      balancedWeight = [u for u in childFrequency if childFrequency[u] > 1]
      if len(unbalancedWeight) > 0:
        childIndex = childWeights.index(unbalancedWeight[0])
        adjustment = self.unbalancedAdjustment(program.children[childIndex])
        if adjustment == 0:
          return program.children[childIndex].weight + (balancedWeight[0] - unbalancedWeight[0])
        return adjustment

    # This exists to pass the result through nodes with < 3 children
    for child in program.children:
      adjustment = self.unbalancedAdjustment(child)
      if adjustment != 0:
        return adjustment

    return 0

  def findTreeWeight(self, program):
    return program.weight + sum([self.findTreeWeight(child) for child in program.children])

  def parseTowerProgram(self, s):
    child_result = (s + '->').split('->')
    name_result = [c.strip() for c in child_result[0].split(' ')]

    name = name_result[0]
    weight = int(name_result[1].strip('()'))
    childNames = [c.strip() for c in child_result[1].split(',') if c != '']
    return Program(name,weight,childNames)

  def getTowerResult(self):
    return self.tower.name

  def getTowerResultExtra(self):
    return self.unbalancedAdjustment(self.tower)


if __name__=='__main__':
  print(Advent07().getTowerResult())
  print(Advent07().getTowerResultExtra())


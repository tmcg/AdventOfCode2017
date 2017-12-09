
# Puzzle 8: I Heard You Like Registers
# http://adventofcode.com/2017/day/8

class Instruction:
  def __init__(self, s):
    tokens = s.split()
    self.register = tokens[0]
    self.increment = int(tokens[2])*-1 if tokens[1] == 'dec' else int(tokens[2])
    self.condRegister = tokens[4]
    self.condOperator = tokens[5]
    self.condValue = int(tokens[6])

  def evalCondition(self, compareValue):
    return self.conditionFunction()(compareValue, self.condValue)

  def conditionFunction(self):
    if self.condOperator == '==':
      return lambda a,b: a == b
    if self.condOperator == '!=':
      return lambda a,b: a != b
    if self.condOperator == '>=':
      return lambda a,b: a >= b
    if self.condOperator == '>':
      return lambda a,b: a > b
    if self.condOperator == '<=':
      return lambda a,b: a <= b
    if self.condOperator == '<':
      return lambda a,b: a < b
    return lambda: False



class Advent08:
  def __init__(self,instructions = []):
    instructions = instructions or self.loadSampleData()
    self.instructions = [Instruction(i) for i in instructions]
    self.registers = {}
    self.highest = 0

  def loadSampleData(self):
    raw = open("./data/advent08.txt").read()
    return [line for line in raw.split("\n")]

  def executeProgram(self):
    for instruction in self.instructions:
      if instruction.evalCondition(self.registers.get(instruction.condRegister,0)):
        currentValue = self.registers.get(instruction.register,0)
        newValue = currentValue + instruction.increment
        self.registers[instruction.register] = newValue
        self.highest = max(self.highest, newValue)

  def getRegisterResult(self):
    self.executeProgram()
    return max(self.registers.values())

  def getRegisterResultExtra(self):
    self.executeProgram()
    return self.highest


if __name__=='__main__':
  print(Advent08().getRegisterResult())
  print(Advent08().getRegisterResultExtra())


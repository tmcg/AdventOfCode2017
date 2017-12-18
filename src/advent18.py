
# Puzzle 18: Duet
# http://adventofcode.com/2017/day/18

class Instruction:
  def __init__(self, opcode, operand1 = None, operand2 = None):
    self.opcode = opcode
    self.operand1 = operand1
    self.operand2 = operand2


class Machine:
  def __init__(self, program = []):
    self.registers = {}
    self.instptr = 0
    self.program = self.decode(program)
    self.currFreq = 0
    self.lastFreq = 0
    self.break1 = False

  def decode(self, program):
    result = []
    for code in program:
      vals = code.split(" ")
      opcode = vals[0]
      operand1 = None if len(vals) < 2 else vals[1]
      operand2 = None if len(vals) < 3 else vals[2]
      result.append(Instruction(opcode,operand1,operand2))

    return result

  def getVal(self, ref):
    try:
      return long(ref) # ref is a literal
    except:
      return self.registers.get(ref,0L) # ref is a register

  def setVal(self, ref, val):
    self.registers[ref] = val

  def fetch(self):
    if self.instptr < 0 or self.instptr >= len(self.program):
      return None

    return self.program[self.instptr]

  def breakpoints(self, inst):
    if inst.opcode == 'rcv' and self.getVal(inst.operand1) != 0:
      self.break1 = True  # break for part 1

  def step(self, inst = None):
    if inst == None:
      inst = self.fetch()

    if inst == None:
      return False

    self.breakpoints(inst)

    if inst.opcode == 'nop':
      self.instptr += 1
    elif inst.opcode in ['set','add','mul','mod']:
      self.instptr += 1
      rx = inst.operand1
      vx = self.getVal(inst.operand1)
      vy = self.getVal(inst.operand2)
      if inst.opcode == 'set':
        vx = vy
      elif inst.opcode == 'add':
        vx = vx + vy
      elif inst.opcode == 'mul':
        vx = vx * vy
      elif inst.opcode == 'mod':
        vx = vx % vy
      self.setVal(rx, vx)
    elif inst.opcode == 'snd':
      self.instptr += 1
      self.currFreq = self.getVal(inst.operand1)
    elif inst.opcode == 'rcv':
      self.instptr += 1
      if self.getVal(inst.operand1) != 0:
        self.lastFreq = self.currFreq
    elif inst.opcode == 'jgz':
      if self.getVal(inst.operand1) > 0:
        self.instptr += self.getVal(inst.operand2)
      else:
        self.instptr += 1

    return True


class Advent18:
  def __init__(self, prog = None):
    self.m1 = Machine(prog) if prog != None else Machine(self.loadSampleData())

  def loadSampleData(self):
    raw = open("./data/advent18.txt").read()
    return [line for line in raw.split("\n")]

  def getDuetResult(self):
    c = True
    while c:
      c = self.m1.step()
      if self.m1.break1:
        return self.m1.lastFreq

  def getDuetResultExtra(self):
    return 0


if __name__=='__main__':
  print(Advent18().getDuetResult())
  print(Advent18().getDuetResultExtra())

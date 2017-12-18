
# Puzzle 18: Duet
# http://adventofcode.com/2017/day/18

from Queue import Queue

class Instruction:
  def __init__(self, opcode, operand1 = None, operand2 = None):
    self.opcode = opcode
    self.operand1 = operand1
    self.operand2 = operand2


class Machine:
  def __init__(self, program = [], pid = None, sendQ = None, recvQ = None):
    self.registers = {}
    self.instptr = 0
    self.program = self.decode(program)
    self.currVal = 0L
    self.lastVal = 0L
    self.break1 = False
    self.blocked = False
    self.sendCount = 0
    self.recvCount = 0
    self.sendQ = sendQ
    self.recvQ = recvQ
    self.pid = pid
    if pid != None:
      self.setVal('p', pid)

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
    self.registers[ref] = long(val)

  def fetch(self):
    if self.instptr < 0 or self.instptr >= len(self.program):
      return None
    return self.program[self.instptr]

  def breakpoints(self, inst):
    if inst.opcode == 'rcv' and self.getVal(inst.operand1) != 0:
      self.break1 = True  # break for part 1

  def send(self, inst):
    self.currVal = self.getVal(inst.operand1)
    self.sendCount += 1
    self.instptr += 1

    if self.sendQ != None:
      self.sendQ.put(self.currVal)

  def recv(self, inst):
    if self.getVal(inst.operand1) != 0:
        self.lastVal = self.currVal
    self.recvCount += 1
    self.instptr += 1

    if self.recvQ != None:
      if self.recvQ.empty():
        self.blocked = True
        self.instptr -= 1
        return True  # blocked
      else:
        self.blocked = False
        self.setVal(inst.operand1,self.recvQ.get())

  def step(self, inst = None):
    # print('pid('+str(self.pid)+'),ip='+str(self.instptr)+',sends='+str(self.sendCount))
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
      self.send(inst)
    elif inst.opcode == 'rcv':
      self.recv(inst)
    elif inst.opcode == 'jgz':
      op1 = self.getVal(inst.operand1)
      op2 = self.getVal(inst.operand2)
      self.instptr += op2 if op1 > 0 else 1

    return True


class Advent18:
  def __init__(self, prog = None):
    self.m0 = Machine(prog,0) if prog != None else Machine(self.loadSampleData(),0)
    self.m1 = Machine(prog,1) if prog != None else Machine(self.loadSampleData(),1)

  def loadSampleData(self):
    raw = open("./data/advent18.txt").read()
    return [line for line in raw.split("\n")]

  def getDuetResult(self):
    c = True
    while c:
      c = self.m0.step()
      if self.m0.break1:
        return self.m0.lastVal

  def getDuetResultExtra(self):
    q0 = Queue()
    q1 = Queue()
    self.m0.recvQ = q0
    self.m1.recvQ = q1
    self.m0.sendQ = q1
    self.m1.sendQ = q0

    progs = [self.m0,self.m1]
    deadlock = False
    while len(progs) > 0 and not deadlock:
      c = progs[0].step()
      if c == False:
        progs.remove(progs[0])
      deadlock = sum([1 if p.blocked else 0 for p in progs]) == len(progs)
      progs.reverse()

    return self.m1.sendCount

if __name__=='__main__':
  print(Advent18().getDuetResult())
  print(Advent18().getDuetResultExtra())

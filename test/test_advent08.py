
from src.advent08 import Advent08
import unittest

class TestAdvent08(unittest.TestCase):
  def testParseInstruction(self):
    t = Advent08([
      'a inc 99 if c > -2',
      'b dec 313 if e >= 6',
      'c inc -36 if f < 0',
      'd dec -42 if b <= 4',
      'e dec 0 if d == 360',
      'f inc 0 if a != -5'
    ])

    instr = t.instructions
    self.assertEqual(len(instr),6)
    # register
    self.assertEqual([i.register for i in instr],['a','b','c','d','e','f'])
    # increment
    self.assertEqual([i.increment for i in instr],[99,-313,-36,42,0,0])
    # conditional register
    self.assertEqual([i.condRegister for i in instr],['c','e','f','b','d','a'])
    # conditional processing
    self.assertEqual([instr[0].evalCondition(v) for v in [-3,-2,-1]],[False,False,True])
    self.assertEqual([instr[1].evalCondition(v) for v in [5,6,7]],[False,True,True])
    self.assertEqual([instr[2].evalCondition(v) for v in [-1,0,1]],[True,False,False])
    self.assertEqual([instr[3].evalCondition(v) for v in [3,4,5]],[True,True,False])
    self.assertEqual([instr[4].evalCondition(v) for v in [359,360,361]],[False,True,False])
    self.assertEqual([instr[5].evalCondition(v) for v in [-6,-5,-4]],[True,False,True])

  def testExecuteProgram(self):
    t = Advent08(['a inc 20 if a == 0','a dec 5 if a == 20'])
    self.assertEqual(t.getRegisterResult(),15)

    t = Advent08(['a inc 20 if a == 0', 'a dec 5 if a == 20'])
    self.assertEqual(t.getRegisterResultExtra(),20)

  def testResult(self):
    t = Advent08()
    self.assertEqual(t.getRegisterResult(),5102)

  def testResultExtra(self):
    t = Advent08()
    self.assertEqual(t.getRegisterResultExtra(),6056)

TestAdvent08.day8 = True
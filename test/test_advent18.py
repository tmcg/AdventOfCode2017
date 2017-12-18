
from src.advent18 import Advent18, Machine, Instruction
import unittest

class TestAdvent18(unittest.TestCase):
  def testInstruction(self):
    aa = Instruction('set','a','31')
    self.assertEqual(aa.opcode,'set')
    self.assertEqual(aa.operand1,'a')
    self.assertEqual(aa.operand2,'31')

  def testDecode(self):
    m = Machine(['set a 31','set b c','jgz p p','nop','snd x'])
    aa = m.program[0]
    self.assertEqual(aa.opcode,'set')
    self.assertEqual(aa.operand1,'a')
    self.assertEqual(aa.operand2,'31')
    bb = m.program[1]
    self.assertEqual(bb.opcode,'set')
    self.assertEqual(bb.operand1,'b')
    self.assertEqual(bb.operand2,'c')
    cc = m.program[2]
    self.assertEqual(cc.opcode,'jgz')
    self.assertEqual(cc.operand1,'p')
    self.assertEqual(cc.operand2,'p')
    dd = m.program[3]
    self.assertEqual(dd.opcode,'nop')
    self.assertEqual(dd.operand1,None)
    self.assertEqual(dd.operand2,None)
    ee = m.program[4]
    self.assertEqual(ee.opcode,'snd')
    self.assertEqual(ee.operand1,'x')
    self.assertEqual(ee.operand2,None)

  def testExecute(self):
    m = Machine(['set a 3', 'add b 4', 'mul a b', 'mod a 10', 'nop', 'snd a'])
    self.assertEqual(len(m.program),6)
    c = m.step()
    self.assertEqual(m.registers,{'a': 3})
    self.assertEqual(m.currFreq,0)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 3, 'b': 4})
    self.assertEqual(m.currFreq,0)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 12, 'b': 4})
    self.assertEqual(m.currFreq,0)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 2, 'b': 4})
    self.assertEqual(m.currFreq,0)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 2, 'b': 4})
    self.assertEqual(m.currFreq,0)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 2, 'b': 4})
    self.assertEqual(m.currFreq,2)
    self.assertEqual(c,True)
    c = m.step()
    self.assertEqual(m.registers,{'a': 2, 'b': 4})
    self.assertEqual(m.currFreq,2)
    self.assertEqual(c,False)

  def testResult(self):
    t = Advent18()
    self.assertEqual(t.getDuetResult(),7071L)

  def testResultExtra(self):
    t = Advent18()
    self.assertEqual(t.getDuetResultExtra(),0)

TestAdvent18.day18 = True

from src.advent17 import Advent17
import unittest

class TestAdvent17(unittest.TestCase):
  def testSpin(self):
    t = Advent17()
    self.assertEqual(t.buffer,[0])
    self.assertEqual(t.pos,0)
    t.spin(3)
    self.assertEqual(t.buffer,[0,1])
    self.assertEqual(t.pos,1)
    t.spin(3)
    self.assertEqual(t.buffer,[0,2,1])
    self.assertEqual(t.pos,1)
    t.spin(3)
    self.assertEqual(t.buffer,[0,2,3,1])
    self.assertEqual(t.pos,2)
    t.spin(3)
    self.assertEqual(t.buffer,[0,2,4,3,1])
    self.assertEqual(t.pos,2)
    t.spin(3)
    self.assertEqual(t.buffer,[0,5,2,4,3,1])
    self.assertEqual(t.pos,1)
    t.spin(3)
    self.assertEqual(t.buffer,[0,5,2,4,3,6,1])
    self.assertEqual(t.pos,5)
    t.spin(3)
    self.assertEqual(t.buffer,[0,5,7,2,4,3,6,1])
    self.assertEqual(t.pos,2)
    t.spin(3)
    self.assertEqual(t.buffer,[0,5,7,2,4,3,8,6,1])
    self.assertEqual(t.pos,6)
    t.spin(3)
    self.assertEqual(t.buffer,[0,9,5,7,2,4,3,8,6,1])
    self.assertEqual(t.pos,1)

  def testResult(self):
    t = Advent17()
    self.assertEqual(t.getSpinlockResult(2017,355),1912)

  def testResultExtra(self):
    t = Advent17()
    self.assertEqual(t.getSpinlockResultExtra(50000000,355),21066990)

TestAdvent17.day17 = True

from src.advent06 import Advent06
import unittest

class TestAdvent06(unittest.TestCase):
  def testFindLargestBank(self):
    t = Advent06([0,0,0])
    self.assertEqual(t.findLargestBank(),0)
    t = Advent06([0,1,1])
    self.assertEqual(t.findLargestBank(),1)
    t = Advent06([0,1,2])
    self.assertEqual(t.findLargestBank(),2)
    t = Advent06([1,1,0])
    self.assertEqual(t.findLargestBank(),0)
    t = Advent06([1,100,1])
    self.assertEqual(t.findLargestBank(),1)

  def testReallocLargestBank(self):
    t = Advent06([0,0,0])
    t.reallocLargestBank()
    self.assertEqual(t.memory,[0,0,0])
    t = Advent06([0,1,1])
    t.reallocLargestBank()
    self.assertEqual(t.memory,[0,0,2])
    t = Advent06([0,1,2])
    t.reallocLargestBank()
    self.assertEqual(t.memory,[1,2,0])
    t = Advent06([1,1,0])
    t.reallocLargestBank()
    self.assertEqual(t.memory,[0,2,0])
    t = Advent06([1,100,1])
    t.reallocLargestBank()
    self.assertEqual(t.memory,[34,33,35])

  def testSamples(self):
    t = Advent06([0,2,7,0])
    self.assertEqual(t.getReallocResult(),5)

  def testSamplesExtra(self):
    t = Advent06([0,2,7,0])
    self.assertEqual(t.getReallocResultExtra(),4)
    t = Advent06([0,2,7,0,9])
    # => 0,2,7,0,9 => 2,4,9,2,1 => 4,6,1,4,3 => 5,1,3,5,4 => 1,2,4,6,5 => 2,3,5,1,7
    # => 4,5,6,2,1 => 5,6,1,4,2 => 6,1,3,5,3 => 1,3,4,6,4 => 2,3,5,1,7
    self.assertEqual(t.getReallocResult(),11)
    t = Advent06([0,2,7,0,9])
    self.assertEqual(t.getReallocResultExtra(),5)

  def testResult(self):
    t = Advent06()
    self.assertEqual(t.getReallocResult(),12841)

  def testResultExtra(self):
    t = Advent06()
    self.assertEqual(t.getReallocResultExtra(),8038)

TestAdvent06.day6 = True
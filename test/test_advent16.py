
from src.advent16 import Advent16
import unittest

class TestAdvent16(unittest.TestCase):
  def testDancing(self):
    t = Advent16([],5)
    lts = lambda x: ''.join(x)
    self.assertEqual(lts(t.programs),'abcde')
    t.step('s1')
    self.assertEqual(lts(t.programs),'eabcd')
    t.step('x3/4')
    self.assertEqual(lts(t.programs),'eabdc')
    t.step('pe/b')
    self.assertEqual(lts(t.programs),'baedc')

  def testResult(self):
    t = Advent16()
    self.assertEqual(t.getPermutationResult(),'pkgnhomelfdibjac')

  def testResultExtra(self):
    t = Advent16()
    self.assertEqual(t.getPermutationResultExtra(),'pogbjfihclkemadn')

TestAdvent16.day16 = True
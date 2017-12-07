
from src.advent07 import Advent07
import unittest

class TestAdvent07(unittest.TestCase):
  def testParseTowerProgram(self):
    t = Advent07([])
    r = t.parseTowerProgram('abcd (100)')
    self.assertEqual(r.name, 'abcd')
    self.assertEqual(r.weight, 100)
    self.assertEqual(r.childNames, [])
    r = t.parseTowerProgram('abcd (100) -> efgh')
    self.assertEqual(r.name, 'abcd')
    self.assertEqual(r.weight, 100)
    self.assertEqual(r.childNames, ['efgh'])
    r = t.parseTowerProgram('abcd (100) -> efgh, ijkl, mnop')
    self.assertEqual(r.name, 'abcd')
    self.assertEqual(r.weight, 100)
    self.assertEqual(r.childNames, ['efgh','ijkl','mnop'])

  def testAssembleTower(self):
    t = Advent07(['abcd (100)'])
    self.assertEqual(t.tower.name, 'abcd')
    self.assertEqual(t.tower.weight, 100)
    self.assertEqual(len(t.tower.children), 0)

    t = Advent07(['abcd (100) -> efgh, ijkl', 'efgh (20)', 'ijkl (30)'])
    self.assertEqual(t.tower.name, 'abcd')
    self.assertEqual(t.tower.weight, 100)
    self.assertEqual(len(t.tower.children), 2)

    t = Advent07(['abcd (100) -> efgh', 'efgh (20) -> ijkl', 'ijkl (30)'])
    self.assertEqual(t.tower.name, 'abcd')
    self.assertEqual(t.tower.weight, 100)
    self.assertEqual(len(t.tower.children), 1)
    self.assertEqual(t.tower.children[0].name, 'efgh')
    self.assertEqual(t.tower.children[0].weight, 20)
    self.assertEqual(len(t.tower.children[0].children), 1)

    self.assertEqual(t.tower.children[0].children[0].name, 'ijkl')
    self.assertEqual(t.tower.children[0].children[0].weight, 30)
    self.assertEqual(len(t.tower.children[0].children[0].children), 0)

  def testUnbalancedAdjustment(self):
    t = Advent07(['a (10)'])
    self.assertEqual(t.unbalancedAdjustment(t.tower),0) # No adjustment required
    t = Advent07(['a (10) -> b', 'b (10)'])
    self.assertEqual(t.unbalancedAdjustment(t.tower),0) # No adjustment required
    t = Advent07(['a (10) -> b', 'b (10) -> c,d,e','c (20) -> f', 'd (30)', 'e (20) -> g', 'f (10)', 'g (9)'])
    self.assertEqual(t.unbalancedAdjustment(t.tower),21) # adjust E from 20 to 21
    t = Advent07(['a (10) -> b', 'b (10) -> c,d,e','c (20) -> f', 'd (30)', 'e (29)', 'f (10)'])
    self.assertEqual(t.unbalancedAdjustment(t.tower),30) # adjust E from 29 to 30

  def testResult(self):
    t = Advent07()
    self.assertEqual(t.getTowerResult(),'eqgvf')

  def testResultExtra(self):
    t = Advent07()
    self.assertEqual(t.getTowerResultExtra(),757)

TestAdvent07.day7 = True
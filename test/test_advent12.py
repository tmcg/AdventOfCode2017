
from src.advent12 import Advent12
import unittest

class TestAdvent12(unittest.TestCase):
  def testParsePipe(self):
    t = Advent12([])
    p = t.parsePipe('1 <-> 2')
    self.assertEqual(p['name'],1)
    self.assertEqual(p['conns'],[2])
    p = t.parsePipe('3 <-> 4, 5')
    self.assertEqual(p['name'],3)
    self.assertEqual(p['conns'],[4,5])

  def testAssembleNetwork(self):
    debug = False
    t = Advent12(['1 <-> 2', '2 <-> 3, 4', '3 <-> 5', '6 <-> 7','8 <-> 9'])
    t.debugNetwork('network1.dot' if debug else None)
    self.assertEqual(t.network.number_of_nodes(),9)
    self.assertEqual(t.network.number_of_edges(),6)
    self.assertEqual(t.getComponentSize(1),5)
    self.assertEqual(t.getComponentCount(),3)

  def testResult(self):
    t = Advent12()
    self.assertEqual(t.getComponentSize(0),134)

  def testResultExtra(self):
    t = Advent12()
    self.assertEqual(t.getComponentCount(),193)

TestAdvent12.day12 = True
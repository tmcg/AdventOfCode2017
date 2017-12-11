
from src.advent10 import Advent10
import unittest

class TestAdvent10(unittest.TestCase):
  def testLoadParse(self):
    t = Advent10([0,1,2,3,4,5])
    t.initInputs([65])
    self.assertEqual(t.ring,[0,1,2,3,4,5])
    self.assertEqual(t.inputs,[65])

    t = Advent10([0,1,2,3,4,5])
    t.initInputs('A,B',True)
    self.assertEqual(t.ring,[0,1,2,3,4,5])
    self.assertEqual(t.inputs,[65,44,66,17,31,73,47,23])

  def testKnotHash(self):
    t = Advent10([0,1,2,3,4])
    t.initInputs([3])
    t.performKnotHash()
    self.assertEqual(t.ring,[2,1,0,3,4])
    self.assertEqual(t.pos,3)
    self.assertEqual(t.skip,1)

    t = Advent10([0,1,2,3,4])
    t.initInputs([3,4])
    t.performKnotHash()
    self.assertEqual(t.ring,[4,3,0,1,2])
    self.assertEqual(t.pos,3)
    self.assertEqual(t.skip,2)

    t = Advent10([0,1,2,3,4])
    t.initInputs([3,4,1])
    t.performKnotHash()
    self.assertEqual(t.ring,[4,3,0,1,2])
    self.assertEqual(t.pos,1)
    self.assertEqual(t.skip,3)

    t = Advent10([0,1,2,3,4])
    t.initInputs([3,4,1,5])
    t.performKnotHash()
    self.assertEqual(t.ring,[3,4,2,1,0])
    self.assertEqual(t.pos,4)
    self.assertEqual(t.skip,4)

  def testDenseHash(self):
    t = Advent10([0,1,2,3,4,5])
    self.assertEqual(t.denseHash(3),'0302')
    self.assertEqual(t.denseHash(2),'010101')
    self.assertEqual(t.denseHash(6),'01')

  def testKnotHashExtra(self):
    t = Advent10()
    t.initInputs('',True)
    t.performKnotHash(64)
    self.assertEqual(t.denseHash(), 'a2582a3a0e66e6e86e3812dcb672a272')

    t = Advent10()
    t.initInputs('AoC 2017',True)
    t.performKnotHash(64)
    self.assertEqual(t.denseHash(), '33efeb34ea91902bb2f59c9920caa6cd')

    t = Advent10()
    t.initInputs('1,2,3',True)
    t.performKnotHash(64)
    self.assertEqual(t.denseHash(), '3efbe78a8d82f29979031a4aa0b16a9d')

    t = Advent10()
    t.initInputs('1,2,4',True)
    t.performKnotHash(64)
    self.assertEqual(t.denseHash(), '63960835bcdc130f0b66d7ff4f6a5a8e')

  def testResult(self):
    t = Advent10()
    t.initInputs()
    self.assertEqual(t.getKnotHashResult(),6952)

  def testResultExtra(self):
    t = Advent10()
    t.initInputs(None,True)
    self.assertEqual(t.getKnotHashResultExtra(),'28e7c4360520718a5dc811d3942cf1fd')

TestAdvent10.day10 = True
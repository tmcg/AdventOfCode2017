
from src.advent14 import Advent14
import unittest

class TestAdvent14(unittest.TestCase):
  def testDiskGenerator(self):
    self.assertEqual(Advent14().getKnotHash(''),'a2582a3a0e66e6e86e3812dcb672a272')
    self.assertEqual(Advent14().getKnotHash('AoC 2017'),'33efeb34ea91902bb2f59c9920caa6cd')
    self.assertEqual(Advent14().getKnotHash('1,2,3'),'3efbe78a8d82f29979031a4aa0b16a9d')
    self.assertEqual(Advent14().getKnotHash('1,2,4'),'63960835bcdc130f0b66d7ff4f6a5a8e')

  def testRowArray(self):
    self.assertEqual(Advent14().getBitArray(''),[])
    self.assertEqual(Advent14().getBitArray('1'),[0,0,0,1])
    self.assertEqual(Advent14().getBitArray('2'),[0,0,1,0])
    self.assertEqual(Advent14().getBitArray('ff'),[1,1,1,1,1,1,1,1])

  def testFindRegions(self):
    g1 = [[1,0,1,1],[1,1,1,0],[0,0,0,1],[1,0,1,1]]
    self.assertEqual(Advent14().findContigRegions(g1),3)

  def testResultSample(self):
    self.assertEqual(Advent14().getDefragResult('flqrgnkx'), 8108)

  def testResultSampleExtra(self):
    self.assertEqual(Advent14().getDefragResultExtra('flqrgnkx'),1242)

  def testResult(self):
    self.assertEqual(Advent14().getDefragResult('uugsqrei'),8194)

  def testResultExtra(self):
    self.assertEqual(Advent14().getDefragResultExtra('uugsqrei'),1141)

TestAdvent14.day14 = True
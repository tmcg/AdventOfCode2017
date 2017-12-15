
from src.advent15 import Advent15, Generator
import unittest

class TestAdvent15(unittest.TestCase):
  def testGeneratorA(self):
    a = Generator(65,16807).get(5)
    self.assertEqual(next(a),1092455)
    self.assertEqual(next(a),1181022009)
    self.assertEqual(next(a),245556042)
    self.assertEqual(next(a),1744312007)
    self.assertEqual(next(a),1352636452)

  def testGeneratorB(self):
    b = Generator(8921,48271).get(5)
    self.assertEqual(next(b),430625591)
    self.assertEqual(next(b),1233683848)
    self.assertEqual(next(b),1431495498)
    self.assertEqual(next(b),137874439)
    self.assertEqual(next(b),285222916)

  def testCompareGenerators(self):
    t = Advent15(65,8921)
    self.assertEqual(t.getDuelResult(5),1)
    self.assertEqual(t.getDuelResult(40000000),588)

  def testCompareGeneratorsExtra(self):
    t = Advent15(65,8921,4,8)
    self.assertEqual(t.getDuelResult(5),0)
    self.assertEqual(t.getDuelResult(1055),0)
    self.assertEqual(t.getDuelResult(1056),1)
    self.assertEqual(t.getDuelResult(5000000),309)

  def testResult(self):
    t = Advent15(277,349)
    self.assertEqual(t.getDuelResult(40000000),592)

  def testResultExtra(self):
    t = Advent15(277,349,4,8)
    self.assertEqual(t.getDuelResult(5000000),320)

TestAdvent15.day15 = True
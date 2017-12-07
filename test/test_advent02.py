
from src.advent02 import Advent02
import unittest

class TestAdvent02(unittest.TestCase):
  def testSamples(self):
    t = Advent02()
    sheet = '5 1 9 5\n7 5 3\n2 4 6 8'
    self.assertEqual(t.getCheckSumResult(sheet),18)

  def testSamplesExtra(self):
    t = Advent02()
    sheet = '5 9 2 8\n9 4 7 3\n3 8 6 5'
    self.assertEqual(t.getCheckSumResultExtra(sheet),9)

  def testResult(self):
    t = Advent02()
    d = t.loadSampleData()
    self.assertEqual(t.getCheckSumResult(d), 42299)

  def testResultExtra(self):
    t = Advent02()
    d = t.loadSampleData()
    self.assertEqual(t.getCheckSumResultExtra(d), 277)

TestAdvent02.day2 = True
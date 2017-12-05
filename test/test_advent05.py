
from src.advent05 import Advent05
import unittest

class TestAdvent05(unittest.TestCase):
  def testSamples(self):
    t = Advent05()
    self.assertEqual(t.getTrampolineResult([0,3,0,1,-3]),5)

  def testSamplesExtra(self):
    t = Advent05()
    self.assertEqual(t.getTrampolineResultExtra([0,3,0,1,-3]),10)

  def testResult(self):
    t = Advent05()
    d = t.loadSampleData()
    self.assertEqual(t.getTrampolineResult(d),387096)

  def testResultExtra(self):
    t = Advent05()
    d = t.loadSampleData()
    self.assertEqual(t.getTrampolineResultExtra(d),28040648)

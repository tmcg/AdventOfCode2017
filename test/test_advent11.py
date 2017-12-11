
from src.advent11 import Advent11
import unittest

class TestAdvent11(unittest.TestCase):
  def testHexPath(self):
    self.assertEqual(Advent11(['ne']).getHexPathResult(),1)
    self.assertEqual(Advent11(['ne','ne']).getHexPathResult(),2)
    self.assertEqual(Advent11(['ne','ne','ne']).getHexPathResult(),3)
    self.assertEqual(Advent11(['ne','ne','sw','sw']).getHexPathResult(),0)
    self.assertEqual(Advent11(['ne','ne','s','s']).getHexPathResult(),2)
    self.assertEqual(Advent11(['se','sw','se','sw','sw']).getHexPathResult(),3)

  def testResult(self):
    self.assertEqual(Advent11().getHexPathResult(),722)

  def testResultExtra(self):
    self.assertEqual(Advent11().getHexPathResultExtra(),1551)

TestAdvent11.day11 = True
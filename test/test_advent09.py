
from src.advent09 import Advent09
import unittest

class TestAdvent09(unittest.TestCase):
  def testCountGroups(self):
    self.assertEqual(Advent09('{}').countGroups(), 1)
    self.assertEqual(Advent09('{{{}}}').countGroups(),6)
    self.assertEqual(Advent09('{{},{}}').countGroups(),5)
    self.assertEqual(Advent09('{{{},{},{{}}}}').countGroups(),16)
    self.assertEqual(Advent09('{<a>,<a>,<a>,<a>}').countGroups(),1)
    self.assertEqual(Advent09('{{<ab>},{<ab>},{<ab>},{<ab>}}').countGroups(),9)
    self.assertEqual(Advent09('{{<!!>},{<!!>},{<!!>},{<!!>}}').countGroups(),9)
    self.assertEqual(Advent09('{{<a!>},{<a!>},{<a!>},{<ab>}}').countGroups(),3)

  def testCountGarbage(self):
    self.assertEqual(Advent09('<>').countGarbage(), 0)
    self.assertEqual(Advent09('<random characters>').countGarbage(), 17)
    self.assertEqual(Advent09('<<<<>').countGarbage(), 3)
    self.assertEqual(Advent09('<{!>}>').countGarbage(), 2)
    self.assertEqual(Advent09('<!!>').countGarbage(), 0)
    self.assertEqual(Advent09('<!!!>>').countGarbage(), 0)
    self.assertEqual(Advent09('<{o"i!a,<{i<a>').countGarbage(), 10)

  def testResult(self):
    self.assertEqual(Advent09().countGroups(),11347)

  def testResultExtra(self):
    t = Advent09()
    self.assertEqual(t.countGarbage(),5404)

TestAdvent09.day9 = True
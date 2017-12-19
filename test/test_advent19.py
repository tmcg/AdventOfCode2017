
from src.advent19 import Advent19
import unittest

testRows = [
  '     |      ',
  '     |  +--+',
  '     A  |  C',
  ' F---|----E|--+',
  '     |  |  |  D',
  '     +B-+  +--+'
]

class TestAdvent19(unittest.TestCase):
  def testDecodeBoard(self):
    t = Advent19(testRows)
    self.assertEqual(t.board,[
      [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '+', '-', '-', '+', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', 'A', ' ', ' ', '|', ' ', ' ', 'C', ' ', ' ', ' '],
      [' ', 'F', '-', '-', '-', '|', '-', '-', '-', '-', 'E', '|', '-', '-', '+'],
      [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', '|', ' ', ' ', 'D'],
      [' ', ' ', ' ', ' ', ' ', '+', 'B', '-', '+', ' ', ' ', '+', '-', '-', '+']
    ])

  def testFollowPath(self):
    t = Advent19(testRows)
    self.assertEqual(t.pos,(5,0))

    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(5,1))
    self.assertEqual(t.pointing,2)
    self.assertEqual(t.letters,'')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(5,2))
    self.assertEqual(t.pointing,2)
    self.assertEqual(t.letters,'A')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(5,5))
    self.assertEqual(t.pointing,2)
    self.assertEqual(t.letters,'A')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(6,5))
    self.assertEqual(t.pointing,1)
    self.assertEqual(t.letters,'AB')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(8,5))
    self.assertEqual(t.pointing,1)
    self.assertEqual(t.letters,'AB')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(8,3))
    self.assertEqual(t.pointing,0)
    self.assertEqual(t.letters,'AB')

    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.step(),True)
    self.assertEqual(t.pos,(9,1))
    self.assertEqual(t.pointing,1)
    self.assertEqual(t.letters,'AB')

    for s in range(24):
      self.assertEqual(t.step(),True)

    self.assertEqual(t.pos,(1,3))
    self.assertEqual(t.pointing,3)
    self.assertEqual(t.letters,'ABCDEF')
    self.assertEqual(t.step(),False)

  def testResult(self):
    t = Advent19()
    self.assertEqual(t.getTubesResult(),'NDWHOYRUEA')

  def testResultExtra(self):
    t = Advent19()
    self.assertEqual(t.getTubesResultExtra(),17540)

TestAdvent19.day19 = True
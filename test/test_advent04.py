
from src.advent04 import Advent04
import unittest

class TestAdvent04(unittest.TestCase):
  def testDuplicates(self):
    t = Advent04()
    self.assertFalse(t.hasDuplicates('aa bb cc dd ee'))
    self.assertTrue(t.hasDuplicates('aa bb cc dd aa'))
    self.assertFalse(t.hasDuplicates('aa bb cc dd aaa'))

  def testAnagramDuplicates(self):
    t = Advent04()
    self.assertFalse(t.hasAnagramDuplicates('abcde fghij'))
    self.assertTrue(t.hasAnagramDuplicates('abcde xyz ecdab'))
    self.assertFalse(t.hasAnagramDuplicates('a ab abc abd abf abj'))
    self.assertFalse(t.hasAnagramDuplicates('iiii oiii ooii oooi oooo'))
    self.assertTrue(t.hasAnagramDuplicates('oiii ioii iioi iiio'))


  def testResult(self):
    t = Advent04()
    d = t.loadSampleData()
    self.assertEqual(t.getPassphraseResult(d),466)

  def testResultExtra(self):
    t = Advent04()
    d = t.loadSampleData()
    self.assertEqual(t.getPassphraseResultExtra(d),251)

TestAdvent04.day4 = True
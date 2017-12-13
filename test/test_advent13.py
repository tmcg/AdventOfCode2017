
from src.advent13 import Advent13
import unittest

class TestAdvent13(unittest.TestCase):
  def testScannerAtTop(self):
    t = Advent13({0:1,1:2,2:3,3:4})
    self.assertEqual(t.isScannerAtTop(0,0),True)
    self.assertEqual(t.isScannerAtTop(0,1),True)
    self.assertEqual(t.isScannerAtTop(0,2),True)
    self.assertEqual(t.isScannerAtTop(0,3),True)
    self.assertEqual(t.isScannerAtTop(0,4),True)
    self.assertEqual(t.isScannerAtTop(0,5),True)

    self.assertEqual(t.isScannerAtTop(1,0),True)
    self.assertEqual(t.isScannerAtTop(1,1),False)
    self.assertEqual(t.isScannerAtTop(1,2),True)
    self.assertEqual(t.isScannerAtTop(1,3),False)
    self.assertEqual(t.isScannerAtTop(1,4),True)
    self.assertEqual(t.isScannerAtTop(1,5),False)

    self.assertEqual(t.isScannerAtTop(2,0),True)
    self.assertEqual(t.isScannerAtTop(2,1),False)
    self.assertEqual(t.isScannerAtTop(2,2),False)
    self.assertEqual(t.isScannerAtTop(2,3),False)
    self.assertEqual(t.isScannerAtTop(2,4),True)
    self.assertEqual(t.isScannerAtTop(2,5),False)
    self.assertEqual(t.isScannerAtTop(2,6),False)
    self.assertEqual(t.isScannerAtTop(2,7),False)
    self.assertEqual(t.isScannerAtTop(2,8),True)
    self.assertEqual(t.isScannerAtTop(2,9),False)
    self.assertEqual(t.isScannerAtTop(2,10),False)
    self.assertEqual(t.isScannerAtTop(2,11),False)
    self.assertEqual(t.isScannerAtTop(3,12),True)
    self.assertEqual(t.isScannerAtTop(3,13),False)

    self.assertEqual(t.isScannerAtTop(3,0),True)
    self.assertEqual(t.isScannerAtTop(3,1),False)
    self.assertEqual(t.isScannerAtTop(3,2),False)
    self.assertEqual(t.isScannerAtTop(3,3),False)
    self.assertEqual(t.isScannerAtTop(3,4),False)
    self.assertEqual(t.isScannerAtTop(3,5),False)
    self.assertEqual(t.isScannerAtTop(3,6),True)
    self.assertEqual(t.isScannerAtTop(3,7),False)
    self.assertEqual(t.isScannerAtTop(3,8),False)
    self.assertEqual(t.isScannerAtTop(3,9),False)
    self.assertEqual(t.isScannerAtTop(3,10),False)
    self.assertEqual(t.isScannerAtTop(3,11),False)
    self.assertEqual(t.isScannerAtTop(3,12),True)
    self.assertEqual(t.isScannerAtTop(3,13),False)

  def testFirewallResult(self):
    t = Advent13({0:3,1:2,4:4,6:4})
    self.assertEqual(t.getFirewallResult(),24)

  def testFirewallResultExtra(self):
    t = Advent13({0:3,1:2,4:4,6:4})
    self.assertEqual(t.getFirewallResultExtra(),10)

  def testResult(self):
    t = Advent13()
    self.assertEqual(t.getFirewallResult(),2384)

  def testResultExtra(self):
    t = Advent13()
    self.assertEqual(t.getFirewallResultExtra(),3921270)

TestAdvent13.day13 = True
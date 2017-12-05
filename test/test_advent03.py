
from src.advent03 import Advent03
import unittest

class TestAdvent03(unittest.TestCase):
  def testRingSizes(self):
    t = Advent03()
    self.assertEqual(t.getRingSize(1),8)
    self.assertEqual(t.getRingSize(2),16)
    self.assertEqual(t.getRingSize(3),24)
    self.assertEqual(t.getRingSize(4),32)
    self.assertEqual(t.getRingSize(5),40)
    self.assertEqual(t.getRingSize(499),3992)
    self.assertEqual(t.getRingSize(500),4000)
    self.assertEqual(t.getRingSize(501),4008)

  def testRingStarts(self):
    t = Advent03()
    self.assertEqual(t.getRingStart(1),2)
    self.assertEqual(t.getRingStart(2),10)
    self.assertEqual(t.getRingStart(3),26)
    self.assertEqual(t.getRingStart(4),50)
    self.assertEqual(t.getRingStart(5),82)
    self.assertEqual(t.getRingStart(499),994010)
    self.assertEqual(t.getRingStart(500),998002)
    self.assertEqual(t.getRingStart(501),1002002)

  def testRingBoundaries(self):
    t = Advent03()
    self.assertEqual(t.getRingNumber(1),0)
    self.assertEqual(t.getRingNumber(2),1)
    self.assertEqual(t.getRingNumber(3),1)
    self.assertEqual(t.getRingNumber(8),1)
    self.assertEqual(t.getRingNumber(9),1)
    self.assertEqual(t.getRingNumber(10),2)
    self.assertEqual(t.getRingNumber(11),2)
    self.assertEqual(t.getRingNumber(24),2)
    self.assertEqual(t.getRingNumber(25),2)
    self.assertEqual(t.getRingNumber(26),3)
    self.assertEqual(t.getRingNumber(27),3)
    self.assertEqual(t.getRingNumber(48),3)
    self.assertEqual(t.getRingNumber(49),3)
    self.assertEqual(t.getRingNumber(50),4)
    self.assertEqual(t.getRingNumber(51),4)

  def testRing0(self):
    t = Advent03()
    self.assertEqual(t.getRingNumber(1),0)

  def testRing1(self):
    t = Advent03()
    for n in range(2,10):
      self.assertEqual(t.getRingNumber(n),1)
    self.assertEqual(t.getSpiralResult(2),1)
    self.assertEqual(t.getSpiralResult(3),2)
    self.assertEqual(t.getSpiralResult(4),1)
    self.assertEqual(t.getSpiralResult(5),2)
    self.assertEqual(t.getSpiralResult(6),1)
    self.assertEqual(t.getSpiralResult(7),2)
    self.assertEqual(t.getSpiralResult(8),1)
    self.assertEqual(t.getSpiralResult(9),2)

  def testRing2(self):
    t = Advent03()
    for n in range(10,26):
      self.assertEqual(t.getRingNumber(n),2)
    self.assertEqual(t.getSpiralResult(11),2)
    self.assertEqual(t.getSpiralResult(12),3)
    self.assertEqual(t.getSpiralResult(13),4)
    self.assertEqual(t.getSpiralResult(10),3)
    self.assertEqual(t.getSpiralResult(14),3)
    self.assertEqual(t.getSpiralResult(15),2)
    self.assertEqual(t.getSpiralResult(16),3)
    self.assertEqual(t.getSpiralResult(17),4)
    self.assertEqual(t.getSpiralResult(18),3)
    self.assertEqual(t.getSpiralResult(19),2)
    self.assertEqual(t.getSpiralResult(20),3)
    self.assertEqual(t.getSpiralResult(21),4)
    self.assertEqual(t.getSpiralResult(22),3)
    self.assertEqual(t.getSpiralResult(23),2)
    self.assertEqual(t.getSpiralResult(24),3)
    self.assertEqual(t.getSpiralResult(25),4)

  def testRing3(self):
    t = Advent03()
    for n in range(26,50):
      self.assertEqual(t.getRingNumber(n),3)
    self.assertEqual(t.getSpiralResult(26),5)
    self.assertEqual(t.getSpiralResult(27),4)
    self.assertEqual(t.getSpiralResult(28),3)
    self.assertEqual(t.getSpiralResult(29),4)
    self.assertEqual(t.getSpiralResult(30),5)
    self.assertEqual(t.getSpiralResult(31),6)
    self.assertEqual(t.getSpiralResult(32),5)
    self.assertEqual(t.getSpiralResult(33),4)
    self.assertEqual(t.getSpiralResult(34),3)
    self.assertEqual(t.getSpiralResult(35),4)

  def testResult(self):
    t = Advent03()
    self.assertEqual(t.getRingNumber(265149),257)
    self.assertEqual(t.getSpiralResult(265149),438)

  def testResultExtra(self):
    t = Advent03()
    self.assertEqual(t.getSpiralResultExtra(265149),266330)

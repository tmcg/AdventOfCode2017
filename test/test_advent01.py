
from src.advent01 import Advent01
import unittest

class TestAdvent01(unittest.TestCase):
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def testSamples(self):
    t = Advent01()
    self.assertEqual(t.getInverseCaptchaResult('1122'),3)
    self.assertEqual(t.getInverseCaptchaResult('1111'),4)
    self.assertEqual(t.getInverseCaptchaResult('1234'),0)
    self.assertEqual(t.getInverseCaptchaResult('91212129'),9)

  def testSamplesExtra(self):
    t = Advent01()
    self.assertEqual(t.getInverseCaptchaResultExtra('1212'),6)
    self.assertEqual(t.getInverseCaptchaResultExtra('1221'),0)
    self.assertEqual(t.getInverseCaptchaResultExtra('123425'),4)
    self.assertEqual(t.getInverseCaptchaResultExtra('123123'),12)
    self.assertEqual(t.getInverseCaptchaResultExtra('12131415'),4)

  def testResult(self):
    t = Advent01()
    d = t.loadSampleData()
    self.assertEqual(t.getInverseCaptchaResult(d),1029)

  def testResultExtra(self):
    t = Advent01()
    d = t.loadSampleData()
    self.assertEqual(t.getInverseCaptchaResultExtra(d),1220)

TestAdvent01.day1 = True
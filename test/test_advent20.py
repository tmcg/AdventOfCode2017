
from src.advent20 import Advent20
import unittest

class TestAdvent20(unittest.TestCase):
  def testImport(self):
    data = [
      'p=<-3787,-3683,3352>, v=<41,-25,-124>, a=<5,9,1>',
      'p=<6815,2269,3786>, v=<-93,23,38>, a=<-8,-6,-10>'
    ]
    t = Advent20(data)
    self.assertEqual(t.particles[0].dist(),10822)
    self.assertEqual(t.particles[1].dist(),12870)
    t.tick()
    self.assertEqual(t.particles[0].dist(),10669)
    self.assertEqual(t.particles[1].dist(),12814)

  def testSample(self):
    data = [
      'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
      'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'
    ]
    t = Advent20(data)
    self.assertEqual(t.particles[0].dist(),3)
    self.assertEqual(t.particles[1].dist(),4)
    t.tick()
    self.assertEqual(t.particles[0].dist(),4)
    self.assertEqual(t.particles[1].dist(),2)
    t.tick()
    self.assertEqual(t.particles[0].dist(),4)
    self.assertEqual(t.particles[1].dist(),2)
    t.tick()
    self.assertEqual(t.particles[0].dist(),3)
    self.assertEqual(t.particles[1].dist(),8)


  def testResult(self):
    t = Advent20()
    self.assertEqual(t.getSwarmResult(),258)

  def testResultExtra(self):
    t = Advent20()
    self.assertEqual(t.getSwarmResultExtra(),707)

TestAdvent20.day20 = True
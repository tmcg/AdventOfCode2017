
from src.advent21 import Advent21, Artwork
import unittest

class TestAdvent21(unittest.TestCase):
  def testFlipV2(self):
    self.assertEqual(Artwork('../..').flipv().s,'../..')
    self.assertEqual(Artwork('../.#').flipv().s,'.#/..')
    self.assertEqual(Artwork('../#.').flipv().s,'#./..')
    self.assertEqual(Artwork('../##').flipv().s,'##/..')
    self.assertEqual(Artwork('.#/..').flipv().s,'../.#')
    self.assertEqual(Artwork('#./..').flipv().s,'../#.')
    self.assertEqual(Artwork('##/..').flipv().s,'../##')
    self.assertEqual(Artwork('##/##').flipv().s,'##/##')

  def testFlipH2(self):
    self.assertEqual(Artwork('../..').fliph().s,'../..')
    self.assertEqual(Artwork('../.#').fliph().s,'../#.')
    self.assertEqual(Artwork('../#.').fliph().s,'../.#')
    self.assertEqual(Artwork('../##').fliph().s,'../##')
    self.assertEqual(Artwork('.#/..').fliph().s,'#./..')
    self.assertEqual(Artwork('#./..').fliph().s,'.#/..')
    self.assertEqual(Artwork('##/..').fliph().s,'##/..')
    self.assertEqual(Artwork('##/##').fliph().s,'##/##')

  def testFlipV3(self):
    self.assertEqual(Artwork('.../.../...').flipv().s,'.../.../...')
    self.assertEqual(Artwork('..#/.../...').flipv().s,'.../.../..#')
    self.assertEqual(Artwork('.#./.../...').flipv().s,'.../.../.#.')
    self.assertEqual(Artwork('#../.../...').flipv().s,'.../.../#..')
    self.assertEqual(Artwork('..#/..#/...').flipv().s,'.../..#/..#')
    self.assertEqual(Artwork('#../..#/#..').flipv().s,'#../..#/#..')
    self.assertEqual(Artwork('.../.#./.#.').flipv().s,'.#./.#./...')
    self.assertEqual(Artwork('.../#../#.#').flipv().s,'#.#/#../...')
    self.assertEqual(Artwork('.../#../...').flipv().s,'.../#../...')
    self.assertEqual(Artwork('.../.#./...').flipv().s,'.../.#./...')
    self.assertEqual(Artwork('.../..#/...').flipv().s,'.../..#/...')
    self.assertEqual(Artwork('.../###/...').flipv().s,'.../###/...')
    self.assertEqual(Artwork('.../.../###').flipv().s,'###/.../...')
    self.assertEqual(Artwork('###/.../...').flipv().s,'.../.../###')

  def testFlipH3(self):
    self.assertEqual(Artwork('.../.../...').fliph().s,'.../.../...')
    self.assertEqual(Artwork('..#/.../...').fliph().s,'#../.../...')
    self.assertEqual(Artwork('.#./.../...').fliph().s,'.#./.../...')
    self.assertEqual(Artwork('#../.../...').fliph().s,'..#/.../...')
    self.assertEqual(Artwork('..#/..#/...').fliph().s,'#../#../...')
    self.assertEqual(Artwork('#../..#/#..').fliph().s,'..#/#../..#')
    self.assertEqual(Artwork('.../.#./.#.').fliph().s,'.../.#./.#.')
    self.assertEqual(Artwork('.../#../#.#').fliph().s,'.../..#/#.#')
    self.assertEqual(Artwork('.../#../...').fliph().s,'.../..#/...')
    self.assertEqual(Artwork('.../.#./...').fliph().s,'.../.#./...')
    self.assertEqual(Artwork('.../..#/...').fliph().s,'.../#../...')
    self.assertEqual(Artwork('.../###/...').fliph().s,'.../###/...')
    self.assertEqual(Artwork('.../.../###').fliph().s,'.../.../###')
    self.assertEqual(Artwork('###/.../...').fliph().s,'###/.../...')

  def testRotateV2(self):
    self.assertEqual(Artwork('../..').rotate(1).s,'../..')
    self.assertEqual(Artwork('../..').rotate(2).s,'../..')
    self.assertEqual(Artwork('../..').rotate(3).s,'../..')
    self.assertEqual(Artwork('../..').rotate(4).s,'../..')
    self.assertEqual(Artwork('#./..').rotate(1).s,'.#/..')
    self.assertEqual(Artwork('#./..').rotate(2).s,'../.#')
    self.assertEqual(Artwork('#./..').rotate(3).s,'../#.')
    self.assertEqual(Artwork('#./..').rotate(4).s,'#./..')
    self.assertEqual(Artwork('#./.#').rotate(1).s,'.#/#.')
    self.assertEqual(Artwork('#./.#').rotate(2).s,'#./.#')
    self.assertEqual(Artwork('##/##').rotate(2).s,'##/##')

  def testRotateV3(self):
    self.assertEqual(Artwork('.../.../...').rotate(1).s,'.../.../...')
    self.assertEqual(Artwork('.../.../...').rotate(2).s,'.../.../...')
    self.assertEqual(Artwork('.../.../...').rotate(3).s,'.../.../...')
    self.assertEqual(Artwork('.../.../...').rotate(4).s,'.../.../...')
    self.assertEqual(Artwork('#../.../...').rotate(1).s,'..#/.../...')
    self.assertEqual(Artwork('#../.../...').rotate(2).s,'.../.../..#')
    self.assertEqual(Artwork('#../.../...').rotate(3).s,'.../.../#..')
    self.assertEqual(Artwork('#../.../...').rotate(4).s,'#../.../...')
    self.assertEqual(Artwork('.#./.../...').rotate(1).s,'.../..#/...')
    self.assertEqual(Artwork('.#./.../...').rotate(2).s,'.../.../.#.')
    self.assertEqual(Artwork('.#./.../...').rotate(3).s,'.../#../...')
    self.assertEqual(Artwork('.#./.../...').rotate(4).s,'.#./.../...')
    self.assertEqual(Artwork('..#/.../...').rotate(1).s,'.../.../..#')
    self.assertEqual(Artwork('..#/.../...').rotate(2).s,'.../.../#..')
    self.assertEqual(Artwork('..#/.../...').rotate(3).s,'#../.../...')
    self.assertEqual(Artwork('..#/.../...').rotate(4).s,'..#/.../...')
    self.assertEqual(Artwork('..#/.#./...').rotate(1).s,'.../.#./..#')
    self.assertEqual(Artwork('..#/.#./...').rotate(2).s,'.../.#./#..')
    self.assertEqual(Artwork('..#/.#./...').rotate(3).s,'#../.#./...')
    self.assertEqual(Artwork('..#/.#./...').rotate(4).s,'..#/.#./...')

  def testCombine(self):
    self.assertEqual(Artwork('.##/.../...').rotate(1).s,'.../..#/..#')
    self.assertEqual(Artwork('.../..#/..#').rotate(1).s,'.../.../##.')
    self.assertEqual(Artwork('.../.../##.').flipv().s,'##./.../...')
    self.assertEqual(Artwork('.../.../##.').fliph().s,'.../.../.##')
    self.assertEqual(Artwork('.##/.../...').rotate(2).flipv().s,'##./.../...')
    self.assertEqual(Artwork('.##/.../...').rotate(2).fliph().s,'.../.../.##')

  def testRules(self):
    a = Advent21(['../.. => .#./###/##.'])
    self.assertEqual(len(a.rules),1)
    a = Advent21(['#./.. => ..#/.#./#.#'])
    self.assertEqual(len(a.rules),4)
    a = Advent21(['../.. => .#./###/##.','#./.. => ..#/.#./#.#'])
    self.assertEqual(len(a.rules),5)
    a = Advent21()
    self.assertEqual(len(a.rules),492)

  def testTransform(self):
    rules = ['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#']
    a = Advent21(rules)
    a.transform()

  def testResult(self):
    t = Advent21()
    self.assertEqual(t.getFractalResult(),150)

  def testResultExtra(self):
    t = Advent21()
    self.assertEqual(t.getFractalResultExtra(),2606275)

TestAdvent21.day21 = True
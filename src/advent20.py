
# Puzzle 20: Particle Swarm
# http://adventofcode.com/2017/day/20

import re

class Particle:
  def __init__(self, name, pos, vel, acc):
    self.name = name
    self.pos = pos
    self.vel = vel
    self.acc = acc
  def tick(self):
    (ax,ay,az) = self.acc
    (vx,vy,vz) = self.vel
    (px,py,pz) = self.pos
    self.vel = (ax+vx,ay+vy,az+vz)
    self.pos = (ax+vx+px,ay+vy+py,az+vz+pz)
  def dist(self):
    return sum(map(abs,self.pos))
  def __str__(self):
    sp = str(self.pos).ljust(21)
    sv = str(self.vel).ljust(21)
    sa = str(self.acc).ljust(21)
    sd = str(self.dist()).rjust(6)
    return 'N=[{4}] D=[{0}] p={1} v={2} a={3}'.format(sd,sp,sv,sa,self.name)


class Advent20:
  def __init__(self, particles = None):
    rows = particles if particles != None else self.loadSampleData()
    self.particles = self.decodeRows(rows)

  def loadSampleData(self):
    raw = open("./data/advent20.txt").read()
    return [line for line in raw.split("\n")]

  def decodeRows(self, rows):
    result = []
    cre = re.compile('p=<(.*),(.*),(.*)>, v=<(.*),(.*),(.*)>, a=<(.*),(.*),(.*)>')
    for row in rows:
      m = cre.match(row)
      pos = (int(m.group(1)),int(m.group(2)),int(m.group(3)))
      vel = (int(m.group(4)),int(m.group(5)),int(m.group(6)))
      acc = (int(m.group(7)),int(m.group(8)),int(m.group(9)))
      result += [Particle(len(result),pos,vel,acc)]
    return result

  def tick(self):
    for p in self.particles:
      p.tick()

  def getSwarmResult(self):
    lastCount = 0
    lastClosest = 0
    for x in range(1000000):
      self.tick()
      if x % 100 == 0:
        c = self.particles[:]
        c.sort(key=lambda x: x.dist())
        if c[0].name == lastClosest:
          lastCount += 1
          if lastCount >= 100:
            return lastClosest
        else:
          lastClosest = c[0].name
          lastCount = 0
    return None

  def getSwarmResultExtra(self):
    lastCollision = 0
    for x in range(1000000):
      # Dictionary sort each particle by position
      pdict = {}
      for p in self.particles:
        if not pdict.has_key(p.pos):
          pdict[p.pos] = []
        pdict[p.pos] += [p]

      # Identify any collisions
      collisions = sum([pdict[pos] for pos in pdict if len(pdict[pos]) > 1],[])
      # Remove any collisions
      self.particles = [p for p in self.particles if p not in collisions]

      # Wait to determine if there are any further collisions
      lastCollision = 0 if len(collisions) > 0 else (lastCollision + 1)
      if lastCollision >= 100:
        return len(self.particles)
      #print('[' + str(x)+'], lastCollision='+str(lastCollision))
      self.tick()


if __name__=='__main__':
  print(Advent20().getSwarmResult())
  print(Advent20().getSwarmResultExtra())

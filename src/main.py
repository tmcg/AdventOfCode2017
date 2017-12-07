
from advent07 import Advent07

if __name__=='__main__':
  t = Advent07(['a (10) -> b', 'b (10) -> c,d,e','c (20) -> f', 'd (30)', 'e (20) -> g', 'f (10)', 'g (9)'])
  print(t.getTowerResultExtra())

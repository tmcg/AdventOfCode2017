
# Puzzle 12: Digital Plumber
# http://adventofcode.com/2017/day/12

# Pre-requisites:
#   > pip install networkx
#   > pip install pydot
# Debugging:
#   http://www.webgraphviz.com/

import networkx as nx
import networkx.drawing.nx_pydot as nxpd

class Advent12:
  def __init__(self, pipes = None):
    pipes = pipes if pipes != None else self.loadSampleData()
    self.network = self.assembleNetwork(pipes)

  def loadSampleData(self):
    raw = open("./data/advent12.txt").read()
    return [line for line in raw.split("\n")]

  def assembleNetwork(self, all_pipes):
    g = nx.Graph()

    for pipe in [self.parsePipe(p) for p in all_pipes]:
      name = pipe['name']
      g.add_node(name)
      for conn in pipe['conns']:
        g.add_edge(name,conn)

    return g

  def debugNetwork(self, debugDotFile = None):
    if debugDotFile:
      nxpd.write_dot(self.network,debugDotFile)

  def parsePipe(self, s):
    parts = s.split('<->')
    pipe_name = int(parts[0])
    pipe_conns = [int(c) for c in parts[1].split(',')]
    return {'name': pipe_name, 'conns': pipe_conns }

  def getComponentSize(self, node):
    return len(nx.node_connected_component(self.network,node))

  def getComponentCount(self):
    return nx.number_connected_components(self.network)


if __name__=='__main__':
  print(Advent12().getComponentSize(0))
  print(Advent12().getComponentCount())


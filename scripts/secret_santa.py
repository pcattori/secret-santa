import collections
import itertools
import networkx as nx
import random

from load_data import load_participants, load_past_assignments

def From(name):
  return (name, 'from')

def To(name):
  return (name, 'to')

def assign(participants, past_assignments):
  graph = nx.DiGraph()
  graph.add_nodes_from(
    (From(participant) for participant in participants.iterkeys()),
    bipartite=0
  )
  graph.add_nodes_from(
    (To(participant) for participant in participants.iterkeys()),
    bipartite=1
  )
  graph.add_edges_from(
    (From(_from), To(to))
    for _from, to in itertools.permutations(participants.iterkeys(),2)
  )
  graph.remove_edges_from(
    (From(_from), To(to))
    for _from, to in past_assignments.iteritems()
  )

  return {
    _from[0]: to[0]
    for _from, to in nx.bipartite.maximum_matching(graph).iteritems()
    if _from[1] == 'from'
  }

def main():
  participants = load_participants()
  past_assignments = load_past_assignments()

  assignment = assign(participants, past_assignments)
  print assignment
  # Uncomment to actually send emails
  #send_assignment_emails(assignment)

if __name__ == '__main__':
  main()

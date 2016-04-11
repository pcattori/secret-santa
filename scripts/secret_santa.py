import collections
import itertools
import networkx as nx
import random

from load_data import load_participants, load_past_assignments

Participant = collections.namedtuple('Participant', ['name', 'role'])

def From(name):
  return Participant(name, 'from')

def To(name):
  return Participant(name, 'to')

def assign(participants, past_assignments):
  graph = nx.DiGraph()

  from_participants = [From(participant) for participant in participants.iterkeys()]
  graph.add_nodes_from(from_participants, bipartite=0)

  to_participants = [To(participant) for participant in participants.iterkeys()]
  graph.add_nodes_from(to_participants, bipartite=1)

  graph.add_edges_from(
    (From(_from), To(to))
    for _from, to in itertools.permutations(participants.iterkeys(),2)
    if past_assignments.get(_from, None) != to
  )

  return {
    _from.name: to.name
    for _from, to in nx.bipartite.maximum_matching(graph).iteritems()
    if _from.role == 'from'
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

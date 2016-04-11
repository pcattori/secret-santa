import collections
import csv
from email.mime.text import MIMEText
import itertools
import networkx as nx
import random
import smtplib

def load_participants():
  with open('participants.csv', 'rb') as f:
    return {row['name']: row['email'] for row in csv.DictReader(f)}

def load_past_assignments():
  with open('past_assignments.csv', 'rb') as f:
    return {row['from']: row['to'] for row in csv.DictReader(f)}

def assign(participants, past_assignments):
  graph = nx.DiGraph()
  graph.add_nodes_from(participants.iterkeys())
  graph.add_edges_from(itertools.permutations(participants.iterkeys(), 2))
  graph.remove_edges_from(past_assignments.iteritems())

  candidate_cycles = filter(
    lambda cycle: len(cycle) == len(participants),
    nx.simple_cycles(graph)
  )
  assignment_cycle = random.choice(candidate_assignments)
  return dict(zip(assignment_cycle, assignment_cycle[1:] + assignment_cycle[:1]))

def send_assignment_emails(assignment):
  s = smtplib.SMTP('localhost')
  for gift_giver, gift_receiver in assignment.iteritems():
    msg = MIMEText("Your secret santa is {}!".format(gift_receiver))
    msg['Subject'] = 'Secret Santa assignment'
    msg['FROM'] = 'Robo-Santa'
    msg['TO'] = participants[gift_giver]
    s.sendmail('Robo-Santa', [participants[gift_giver], msg.as_string())
  s.quit()

def main():
  participants = load_participants()
  past_assignments = load_past_assignments()

  assignment = assignment(participants, past_assignments)
  # Uncomment to actually send emails
  #send_assignment_emails(assignment)

if __name__ == '__main__':
  main()

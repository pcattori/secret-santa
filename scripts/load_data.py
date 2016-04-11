import csv

def load_participants():
  with open('../data/participants.csv', 'rb') as f:
    return {row['name']: row['email'] for row in csv.DictReader(f)}

def load_past_assignments():
  with open('../data/past_assignments.csv', 'rb') as f:
    return {row['from']: row['to'] for row in csv.DictReader(f)}


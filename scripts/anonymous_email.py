from email.mime.text import MIMEText
import smtplib

def send_assignment_emails(assignment):
  s = smtplib.SMTP('localhost')
  for gift_giver, gift_receiver in assignment.iteritems():
    msg = MIMEText("Your secret santa is {}!".format(gift_receiver))
    msg['Subject'] = 'Secret Santa assignment'
    msg['FROM'] = 'Robo-Santa'
    msg['TO'] = participants[gift_giver]
    s.sendmail('Robo-Santa', [participants[gift_giver], msg.as_string())
  s.quit()

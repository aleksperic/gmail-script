from smtplib import SMTP, SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

server = SMTP_SSL('smtp.gmail.com', 465)

gmail = input('Your gmail address: ')
password = getpass('Password: ')

server.login(gmail, password)
server.ehlo()

msg = MIMEMultipart()
msg['FROM'] = gmail
msg['TO'] = input('TO: ')
msg['SUBJECT'] = input('SUBJECT: ')

message = input('MESSAGE: ')

msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()
server.sendmail('aca.peric93@gmail.com', 'aleksandar.peric@icloud.com', text)
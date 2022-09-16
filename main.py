from smtplib import SMTP, SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass


gmail = input('Your gmail address: ')
password = getpass('Password: ')

server = SMTP_SSL('smtp.gmail.com', 465)
try:
    server.login(gmail, password)
except:
    print("Wrong email or password!")
    exit(1)
finally:
    print('Login successful!')

server.ehlo()

msg = MIMEMultipart()
msg['FROM'] = gmail
msg['TO'] = input('TO: ')
msg['SUBJECT'] = input('SUBJECT: ')

message = input('MESSAGE: ')

msg.attach(MIMEText(message, 'plain'))
text = msg.as_string()

try:
    server.sendmail(msg['FROM'], msg['TO'], text)
except:
    print('Something went wrong!')
    exit(1)
finally:
    server.quit()
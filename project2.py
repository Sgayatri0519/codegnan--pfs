#email
#SMTP(simple mail transfer protocol):this is used to send emails from server to another...
#note:1.SMTP Port-465,2.SMTP TLS Port-587
'''
import smtplib
from emai.lmessage class:sender,mail,resever mail.ect
msg['subject']='SMTP ON mail'
msg['from']='sender@mail.com'
msg['to']='receiver@mail.com'

import smtplib
from email.message import EmailMessage
sender='saimosuru0510@gmail.com'
password='uhklzhpwnjphlwpi'
msg=EmailMessage()

msg['subject']='welcome mail'
msg['from']=sender
msg['to']='nehapriya522@gmail.com'
msg.set_content('oye  my name is sai')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()

'''

import smtplib
from email.message import EmailMessage

sender='saimosuru0510@gmail.com'
password='uhklzhpwnjphlwpi'
reciver=['nehapriya552@gmail.com','rajanasravyasri@gmail.com']
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in reciver:
  msg=EmailMessage()

  msg['subject']='welcome to vizag'
  msg['From']=sender
  msg['To']=email
  msg.set_content('hello')
  server.send_message(msg)
server.quit()  

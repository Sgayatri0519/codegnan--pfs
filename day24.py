#Date and Time:python provides the built in datatime module to work with dates and time
import datetime
today=datetime.date.today()
print(today)
#to access today time
import datetime
today=datetime.date.today()
now=datetime.datetime.now()
print(now)
print(today)
#to acces year
import datetime
now=datetime.datetime.now()
print(f"year is:{now.year}")
print(f"month is:{now.month}")
print(f"day is:{now.day}")
print(f"hour is:{now.hour}")
print(f"minute is:{now.minute}")
print(f"second is:{now.second}")
#formating the date and time
#strftime() is used to formate date and time
#%d:day
#%m:month
#%y:year
#%h:hour
#%mi:minute
#%s:second
import datetime
now=datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
print(now.strftime("%d-%m=%y"))
#
import datetime
date_1=datetime.date(2025,6,1)
date_2=datetime.date(2025,6,1)
differ=date_2-date_1
print(differ)
#timedelta
import datetime
today=datetime.date.today()
future=today+datetime.timedelta(days=7)
print(future)
#returns the readable time datetime and string
import datetime
day_=datetime.date.today()
print(day_.ctime())
#to access the calendar
import calendar
import datetime

today=datetime.date.today()
year=today.year
month=today.month
print(calendar.month(year,month))
#example
import datetime
year=2004
month=11
print(calendar.month(year,month))

#write a program to send email msg  in particular time
import smtplib
from email.message import EmailMessage
sender='saimosuru0510@gmail.com'
password='mgdgzcyddrtuncsv'
reciver=['nehapriya552@gmail.com',]
target_time="10:30"
for email in reciver:
  msg=EmailMessage()

  msg['subject']='happy birthday'
  msg['From']=sender
  msg['To']=email
  msg.set_content('hello')
  server.send_message(msg)
server.quit()  





































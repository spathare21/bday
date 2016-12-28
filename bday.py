import csv
import time
import smtplib
from datetime import datetime

f = open('bday.csv')
store = csv.reader(f)
data = []
for i in store:
	data.append(i)

cur = str(time.strftime("%d-%m"))
curr_date = cur.split("-")
curr_day = curr_date[0]
curr_mon = curr_date[1]

for i in data:
	x = i[1].split("-")
	x.pop()
	if x[1] == curr_mon and x[0] == curr_day:
		sender = 'spathare@redhat.com'
		receivers = ['adasound@redhat.com']

		message = """From: From Sachin <spathare@redhat.com>
		To: To Avinash <adasound@redhat.com>
		Subject: Birthday Greetings

		Wish you a very Happy Birthday !!!
		"""

		try:
		  smtpObj = smtplib.SMTP('localhost')
		  smtpObj.sendmail(sender, receivers, message)
		  print("Successfully sent email")
		except SMTPException:
		  print("Error: unable to send email")
			



	

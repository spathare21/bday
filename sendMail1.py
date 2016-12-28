#!/usr/bin/python

import smtplib

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
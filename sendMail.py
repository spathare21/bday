#!/usr/bin/python

import smtplib


def send_mail():
	sender = 'spathare@redhat.com'
	receivers = ['adasound@redhat.com']

	message = """From: From Person <from@fromdomain.com>
	To: To Person <to@todomain.com>
	Subject: SMTP e-mail test

	This is a test e-mail message.
	"""

	try:
	   smtpObj = smtplib.SMTP('localhost')
	   smtpObj.sendmail(sender, receivers, message)         
	   print "Successfully sent email"
	except SMTPException:
	   print "Error: unable to send email"

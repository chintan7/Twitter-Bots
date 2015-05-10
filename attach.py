#!/usr/bin/python

import smtplib
import base64

filename = "input.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'cmvora@gmail.com'
reciever = 'cvora@umd.com'

marker = "AUNIQUEMARKER"

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """From: From Person <cmvora@gmail.com>
To: To Person <cvora@umd.edu>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3
gmail_user = "cmvora@gmail.com"
gmail_pwd = "Chintan5493"
FROM = 'cmvora@gmail.com'
TO = ['cvora@umd.edu'] #must be a list
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"

try:
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.login(gmail_user, gmail_pwd)
	server.sendmail(FROM, TO, message)
	print "Successfully sent email"
	server.close()
except Exception:
	print "Error: unable to send email"

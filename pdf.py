from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
 
msg = MIMEMultipart()
msg['Subject'] = 'Email From Python jajaja'
msg['From'] = 'cmvora@gmail.com'
msg['Reply-to'] = 'cvora@umd.edu'
msg['To'] = 'cvora@umd.edu'
 
# That is what u see if dont have an email reader:
msg.preamble = 'Multipart massage.\n'
 
# This is the textual part:
part = MIMEText("Hello im sending an email from a python program")
msg.attach(part)
 
# This is the binary part(The Attachment):
part = MIMEApplication(open("file.pdf","rb").read())
part.add_header('Content-Disposition', 'attachment', filename="file.pdf")
msg.attach(part)
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
	server.sendmail(FROM, TO, msg.as_string())
	print "Successfully sent email"
	server.close()
except Exception:
	print "Error: unable to send email"

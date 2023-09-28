import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail Port for SSL: 465
# Gmail Port for TLS/STARTTLS: 587

print("start")
# set up the SMTP server
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
print("conn created ", s.local_hostname)

s.set_debuglevel(1)
s.starttls()
print("TLS enabled ", s.local_hostname)

uname = input("Gmail full username? ")
pwd = input("Gmail Password? ")

s.login(uname, pwd)
print("Login done ", s.local_hostname )

msg = MIMEMultipart()       # create a message
# add in the actual person name to the message template
message = msg.substitute(PERSON_NAME="Faizan Raza")

# setup the parameters of the message
msg['From']='faizan.raza@gmail.com'
msg['To']='faizan.raza@gmail.com'
msg['Subject']="This is TEST"

# add in the message body
msg.attach(MIMEText(message, 'plain'))
print("Mesg created ", s.local_hostname )

# send the message via the server set up earlier.
s.send_message(msg)

print("end")
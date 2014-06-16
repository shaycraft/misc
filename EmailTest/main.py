#!/usr/bin/python
import sys
from sys import argv
import smtplib
from email.mime.text import MIMEText

#if len(argv) != 3:
#    sys.stderr.write('Usage: ' + sys.argv[0] + ' <from_addr> <to_addr>\n')
#   sys.exit(1)

from_addr = "minerals@tcolandservices.com"
to_addr = "phreakdawg@gmail.com"

msg = ""
for line in sys.stdin:
    msg = msg + line
msg = MIMEText(msg)

#msg =  MIMEText(sys.stdin.readlines())

msg['Subject'] = "Mineral Lease Evaluation Form Web Submission"
msg['From'] = str(from_addr)
msg['To'] = str(to_addr)

s = smtplib.SMTP('linuxserver1.tcolandservices.com')

print msg.as_string()

s.sendmail('shaycraft@tcolandservices.com', 'phreakdawg@gmail.com', msg.as_string())

print "Email sent"

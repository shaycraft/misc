import smtplib
from email.mime.text import MIMEText

msg = MIMEText("You suck")

msg['Subject'] = "Python email test"
msg['From'] = "shaycraft@tcolandservices.com"
msg['To'] = "phreakdawg@gmail.com"

s = smtplib.SMTP('linuxserver1.tcolandservices.com')

s.sendmail('shaycraft@tcolandservices.com','phreakdawg@gmail.com',msg.as_string())

print msg.as_string()
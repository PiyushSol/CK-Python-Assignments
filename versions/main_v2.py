import smtplib
from email.message import EmailMessage
msg = EmailMessage()

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('solankipiyush942@gmail.com','osmq loav tnzz ffqw')

receiver_emails = ["aryanaparmar26@gmail.com", "aaryansanjayjagtap@gmail.com"]


msg['From']='solankipiyush942@gmail.com'
msg['To']=", ".join(receiver_emails)
msg['Subject']='Testing Automating Email'

body='This is a test email for automating mails . It works!'

msg.set_content(body)
server.send_message(msg)
server.quit()
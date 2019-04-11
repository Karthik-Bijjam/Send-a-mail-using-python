#! python3

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587) # smtp address and port
conn.ehlo() # call this to start the connection
conn.starttls() # starts tls encryption. When we send our password it will be encrypted.
conn.login('Your Email Address', 'Password')
subject = 'Sample Mail'
msg ="Hai, This is a sample mail, I send using python code"
message = 'Subject: {}\n\n{}'.format(subject,msg)
conn.sendmail('recipient Email Address','recipient Email Address', message)
#conn.sendmail(from_entry.get(),to_entry.get(),msg_entry.get())
conn.quit()
print('Sent notificaton e-mails for the following recipients:\n')

#send e-mail alert
print("Mail Sent")


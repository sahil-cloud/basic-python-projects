import smtplib

# receivers address
to = 'receive email' 

# content here
content = "hey i was trying to send msg with python"

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',25)
    server.ehlo()
    server.starttls()
    server.login('email','password')
    server.sendmail('email,to,content)
    server.close()

sendEmail(to,content)
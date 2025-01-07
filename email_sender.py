import smtplib

to = input("Enter email of recipent:\n")

content = input("Enter the content or mail:\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abcd@gmail.com', 'J587')
    server.sendmail('abcd@gmail.com', to , content)
    server.close()
    
sendEmail(to, content)
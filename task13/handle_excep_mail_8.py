import smtplib
from email.mime.text import MIMEText

try:
    email_sender = input("Enter the sender email id:")
    email_receiver = input("Enter the recepient email id:")

    subject = input("Enter the subject:")
    body = input("Enter the body of the email:")

    message = MIMEText(body)
    message['From'] = email_sender
    message['To'] = email_receiver
    message['Subject'] = subject


    smtp_server = 'sandbox.smtp.mailtrap.io'
    smtp_user = 'fe69ba67cc2233'
    smtp_pass = '11d904a8f7f33d'
    smtp_port = '2525'

    server = smtplib.SMTP(smtp_server, smtp_port)
    print("server",server)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(email_sender, email_receiver,message.as_string())
    print("Email send")

except smtplib.SMTPAuthenticationError:
    print("Authentication Failed")
except smtplib.SMTPConnectError:
    print("Connection Failed")
except smtplib.SMTPException as e:
    print(e)


finally:
    server.quit()
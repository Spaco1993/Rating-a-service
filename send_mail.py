import smtplib
from email.mime.text import MIMEText

def send_mail(client, serviceprovider, ratings, comments):
    port = 587
    smtp_server = 'smtp.mailtrap.io'
    login = 'fc5d12d6e7f243'
    password = '92f4457880803c'
    message = (f"<h3>New Feedback Submission</h3>" f"<ul>" f"<li>Client:{client}</li>"
    f"<li>Serviceprovider:{serviceprovider}</li>" f"<li>Ratings:{ratings}</li>" f"<li>Comments:{comments}</li>" f"</ul>"


    ) 

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Service Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
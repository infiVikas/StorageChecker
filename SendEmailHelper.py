

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

# Assuming you have a logger configured
logger = logging.getLogger(__name__)



def send_email(subject,html):
    try:
        # Email configuration
        email_from = 'nikesh.vishwakarma@infidigit.com'
        to_email = 'vikas.verma@infidigit.com'
        password = "pejk cxqi pdmb lyxg"
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = email_from
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_from, password)
            server.sendmail(email_from, to_email, msg.as_string())

        return "Email sent successfully!"

    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")    








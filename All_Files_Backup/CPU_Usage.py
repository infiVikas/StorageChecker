
from SendEmailHelper import *

import psutil

def get_cpu_usage_percent(interval=1):
    cpu_percent = psutil.cpu_percent(interval=interval)
    return cpu_percent

cpu_usage_in_percentage = get_cpu_usage_percent(interval=1)

if cpu_usage_in_percentage >= 80.0:
    html = f'''
        <html>
            <body>
                <h5>CPU Usage</h5>
                <p>CPU Usage reached 80% </p>
            </body>
        </html>
        '''
    subject = 'Task for CPU'

    resp = send_email(subject,html)
    print("Email Sent successfully!")

else:
    print("CPU Usage email NOT Sent!")




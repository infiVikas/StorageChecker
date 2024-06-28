from SendEmailHelper import *
import psutil

def get_memory_usage_percent():
    virtual_memory = psutil.virtual_memory()
    memory_percent = virtual_memory.percent
    return memory_percent

memory_usage_in_percentage = get_memory_usage_percent()


# To check if memory usage reached 70%
if memory_usage_in_percentage >= 70.0:
    html = f'''
        <html>
            <body>
                <h5>Memory Usage</h5>
                <p>Memory Usage reached 70% </p>
            </body>
        </html>
        '''
    subject = 'Task for Memory'

    resp = send_email(subject,html)
    print("Email Sent successfully!")

else:
    print("Memory Usage Email NOT Sent!")


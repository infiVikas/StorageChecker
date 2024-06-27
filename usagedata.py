from SendEmailHelper import *
import psutil



# ***************************************************** Drive Storage *****************************************************
def get_drive_storage(drive):
    # Get the disk usage for the given drive
    usage = psutil.disk_usage(drive)
    
    # Convert bytes to GB
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)
    percent_used = usage.percent
    return total_gb, used_gb, free_gb, percent_used


# ---------------------------------------------------------------------------------------------------------
def get_C_DriveStorage(drive):
    total, used, free, percent = get_drive_storage(drive)
    C_DriveStoragePercentage = f"{percent:.2f}"
    return C_DriveStoragePercentage

drive = 'C:'
C_drive_storage_in_percent = float(get_C_DriveStorage(drive))


# To 'C' Drive Storage reached 50% then send an Email:
if C_drive_storage_in_percent == 50.0:
    html = f'''
        <html>
            <body>
                <h5> 'C' Drive Storage </h5>
                <p> 'C' Drive Storage reached 50% </p>
            </body>
        </html>
        '''
    subject = "Task for 'C' Drive"

    resp = send_email(subject,html)
    print("'C' Drive Email Sent successfully!")

else:
    print("'C' Drive Email NOT Sent!")


# -----------------------------------------------------------------------------------------------------

# No 'D' Drive in my Laptop
# def get_D_DriveStorage(drive):
#     total, used, free, percent = get_drive_storage(drive)
#     C_DriveStoragePercentage = f"{percent:.2f}"
#     return C_DriveStoragePercentage

# drive = 'D:'
# D_drive_storage_in_percent = float(get_D_DriveStorage(drive))


# # To 'D' Drive Storage reached 40% then send an Email:
# if D_drive_storage_in_percent == 40.0:
#     html = f'''
#         <html>
#             <body>
#                 <h5> 'D' Drive Storage </h5>
#                 <p> 'D' Drive Storage reached 40% </p>
#             </body>
#         </html>
#         '''
#     subject = "Task for 'D' Drive"

#     resp = send_email(subject,html)
#     print("'D' Drive Email Sent successfully!")

# else:
#     print("'D' Drive Email NOT Sent!")




# ***************************************************** CPU Usage *****************************************************

def get_cpu_usage_percent(interval=1):
    cpu_percent = psutil.cpu_percent(interval=interval)
    return cpu_percent

cpu_usage_in_percentage = get_cpu_usage_percent(interval=1)

if cpu_usage_in_percentage == 80.0:
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
    print("CPU Usage Email Sent successfully!")

else:
    print("CPU Usage Email NOT Sent!")



# ***************************************************** Memory Usage *****************************************************

def get_memory_usage_percent():
    virtual_memory = psutil.virtual_memory()
    memory_percent = virtual_memory.percent
    return memory_percent

memory_usage_in_percentage = get_memory_usage_percent()


# To check if memory usage reached 70%
if memory_usage_in_percentage == 70.0:
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
    print("Memory Usage Email Sent successfully!")

else:
    print("Memory Usage Email NOT Sent!")




from SendEmailHelper import *
import psutil

def get_drive_storage(drive):
    # Get the disk usage for the given drive
    usage = psutil.disk_usage(drive)
    
    # Convert bytes to GB
    total_gb = usage.total / (1024 ** 3)
    used_gb = usage.used / (1024 ** 3)
    free_gb = usage.free / (1024 ** 3)
    percent_used = usage.percent
    
    return total_gb, used_gb, free_gb, percent_used




def get_C_DriveStorage(drive):
    total, used, free, percent = get_drive_storage(drive)

    # print(f"Drive: {drive}")
    # print(f"Total: {total:.2f} GB")
    # print(f"Used: {used:.2f} GB")
    # print(f"Free: {free:.2f} GB")
    # print(f"{percent:.2f}")

    C_DriveStoragePercentage = f"{percent:.2f}"
    # print("C_DriveStoragePercentage ------>",C_DriveStoragePercentage)
    return C_DriveStoragePercentage

drive = 'C:'
resp = get_C_DriveStorage(drive)
C_drive_storage_in_percent = float(resp)
print("resp of 'C' Drive in % ---->",C_drive_storage_in_percent)


# To 'C' Drive Storage reached 50% then send an Email:
if C_drive_storage_in_percent >= 50.0:
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
    print("Email Sent successfully!")

else:
    print("Email not Sent!")

# -------------------------------------------------------------------------------------------------------------

# def get_D_DriveStorage(drive):
#     total, used, free, percent = get_drive_storage(drive)

#     print(f"Drive: {drive}")
#     print(f"Total: {total:.2f} GB")
#     print(f"Used: {used:.2f} GB")
#     print(f"Free: {free:.2f} GB")
#     print(f"{percent:.2f}")

#     C_DriveStoragePercentage = f"{percent:.2f}"
#     # print("C_DriveStoragePercentage ------>",C_DriveStoragePercentage)
#     return C_DriveStoragePercentage

# drive = 'D:'
# resp = get_D_DriveStorage(drive)
# D_drive_storage_in_percent = float(resp)
# print("resp of 'D' Drive in % ---->",D_drive_storage_in_percent)


# # To 'D' Drive Storage reached 40% then send an Email:
# if D_drive_storage_in_percent >= 40.0:
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
#     print("Email Sent successfully!")

# else:
#     print("Email not Sent!")
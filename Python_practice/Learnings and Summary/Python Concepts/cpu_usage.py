# Write a Python script to monitor CPU usage:

# Approach - 1:

import psutil
import time

THRESHOLD = 85  # CPU usage threshold in percentage

# while True:
#     cpu_usage = psutil.cpu_percent(interval=1)
#     print(f"Current CPU Usage: {cpu_usage}%")
    
#     if cpu_usage > THRESHOLD:
#         print("Warning: CPU usage is above the threshold!")
    
#     time.sleep(5)  # Check every 5 seconds

# # Approach - 2: Using a function to monitor CPU usage

# def monitor_cpu_usage():
    
#     while True:
#         cpu_usage = psutil.cpu_percent(interval=1)
#         # print(f"Current CPU Usage: {cpu_usage}%")
        
#         if cpu_usage > THRESHOLD:
#             print(f"WARNING: CPU usage is above the threshold: {cpu_usage}%")
#         else: 
#             print(f"CPU usage is within the acceptable range: {cpu_usage}%")
        
#         time.sleep(5)  # Check every 5 seconds

# # Call the function to start monitoring
# monitor_cpu_usage()

# Approach - 3: Using a class to monitor CPU usage:

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)

    if cpu_usage > THRESHOLD:
        print(f"ALERT: CPU usage high -> {cpu_usage}%")
    else:
        print(f"CPU OK -> {cpu_usage}%")

while True:
    check_cpu_usage()  # Pass self as None since we're not using a class here
    time.sleep(10)  # Check every 10 seconds

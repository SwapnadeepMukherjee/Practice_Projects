# How would you write a Python script to monitor CPU, memory, and disk usage on a server?

import psutil
from datetime import time
import time

CPU_THREASHOLD = 85
MEM_THREASHOLD = 85
DISK_THREASHOLD = 85

def server_health_check():
	cpu_usage = psutil.cpu_percent(interval=1)
	mem_usage = psutil.virtual_memory().percent
	disk_ussge = psutil.disk_usage('/').percent
	
if CPU_THREASHOLD > 85:
	print("ALERT! CPU usage has crossed minimum range: {cpu_usage}%")
else:
	print("INFO! CPU usage is normal: {cpu_usage}%")
	
if MEM_THREASHOLD > 85:
	print("ALERT! Memory usage has crossed minimum range: {mem_usage}%")
else:
	print("INFO! Memory usage is normal:, {mem_usage}%")
	
if DISK_THREASHOLD > 85:
	print("ALERT! Disk usage has crossed minimum range: {disk_ussge}%")
else:
	print("INFO! Disk usage is normal: {disk_ussge}%")
	
while True:

	server_health_check()
	time.sleep(10)
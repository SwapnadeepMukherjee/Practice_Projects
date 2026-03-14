# How would you automate server health checks using Python?

# Purpose: Monitor system resources

# Typical checks:

# CPU usage

# Memory usage

# Disk usage

# Network usage

# Example code:

import psutil
import time

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
network = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().

print(cpu, memory, disk, network)
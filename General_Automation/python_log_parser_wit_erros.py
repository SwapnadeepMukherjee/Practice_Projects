# Python Code to Parse Logs and Count Errors:

from collections import Counter

log_file = "app.log"

error_counts = Counter()

with open(log_file, "r") as f:
    for line in f:
        if "ERROR" in line:
            parts = line.split()
            error_type = parts[-1]   # assume error code at end
            error_counts[error_type] += 1

for error, count in error_counts.items():
    print(f"{error}: {count}")
# How would you **automate log parsing using Python?

# To automate log parsing using Python, I would write a script that reads log files line by line, extracts relevant information such as errors or timestamps, and then processes or stores the results for monitoring or alerting.

# Typically, I would use Python modules like re (regular expressions) for pattern matching and file handling to process large log files efficiently.

error_count = 0

with open('logfile.log', 'r') as log_file:
    for line in log_file:
        if 'ERROR' in line:
            error_count += 1
            print(f"Error found: {line.strip()}")

print(f"Total errors found: {error_count}")
# How would you write a Python script to check if a website is up or down?

# To write a Python script that checks if a website is up or down, I would use the `requests` library to send an HTTP GET request to the website and check the response status code. If the status code is 200, it indicates that the website is up; otherwise, it is considered down.

# Here is a simple example of such a script:

import requests
import time

url = "https://www.google.com"

def check_website(url):
	try: 
		response = requests.get(url, timeout=5)
		
		if response.status_code == 200:
			print(f"{url} is UP" )
		elif response.status_code != 200:
			print(f"{url} is DOWN. Status code: {response.status_code}")		
		
	except requests.exceptions.RequestException:
		print(f"{url} is DOWN (connection error)")
		
while True:
	check_website(url)
	time.sleep(10)
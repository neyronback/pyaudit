import requests
import time

# Ask for a sample URL
url = input("Enter the sample URL: ")

# Send 6000 requests per minute
requests_per_minute = 6000
interval = 60 / requests_per_minute

while True:
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    time.sleep(interval)
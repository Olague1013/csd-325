# astronauts.py
# Author: Andrew Olague
# Assignment: Module 9 - APIs
# Description: Retrieve current astronauts and format output.

import requests
import json

# Get data from the API
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

print("Status Code:", response.status_code)

# Print raw JSON response
print("\nRaw Response:")
print(response.text)

# Formatted output
if response.status_code == 200:
    data = response.json()
    print("\nFormatted Output:")
    print(f"Number of people in space: {data['number']}")
    for person in data['people']:
        print(f"- {person['name']} aboard {person['craft']}")
else:
    print("Failed to retrieve data.")

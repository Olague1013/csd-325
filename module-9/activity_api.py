# activity_api.py
# Author: Andrew Olague
# Assignment: Module 9 - APIs
# Description: Using the Cat Facts API to retrieve a random fact.

import requests
import json

url = "https://catfact.ninja/fact"
response = requests.get(url)

print("Status Code:", response.status_code)

print("\nRaw Response:")
print(response.text)

if response.status_code == 200:
    data = response.json()
    print("\nFormatted Output:")
    print("Cat Fact:", data["fact"])
else:
    print("Failed to retrieve data.")

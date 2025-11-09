# api_test.py
# Author: Andrew Olague
# Assignment: Module 9 - APIs
# Date: 11/09/2025
# Description: Testing a basic API connection to Google

import requests

response = requests.get('http://www.google.com')
print("Status Code:", response.status_code)


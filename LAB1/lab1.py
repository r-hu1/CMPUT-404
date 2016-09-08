import requests

response = requests.get("https://github.com/r-hu1/CMPUT-404/raw/master/LAB1/lab1.py")

print response.text

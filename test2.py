import requests
import json
import time

url = "https://api.testmail.app/api/json?apikey=ba7dc8bb-fd50-41f9-b073-547bdabc3e89&namespace=cjwz2&pretty=false"
OLD_EMAILS = []
while True:
    print("Checking for new emails...")
    # get data and print all the new emails
    data = requests.get(url).json()
    for email in data["emails"]:
        if email not in OLD_EMAILS:
            print(email["text"])
            OLD_EMAILS.append(email)
    time.sleep(60)
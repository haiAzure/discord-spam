import requests
import time
import random  # Add this line to import the random module
import threading
import os

def RandomCWord():
    url_list = ["https://github.com/haiAzure/", "discord.com", "skid :)", "ma vương tulen", "ayuly"] 
    return random.choice(url_list)

def RandomChinaWord():
    val = random.randint(0x4e00, 0x9fbf) 
    return chr(val)

def RandomChina(size: int):
    words = ""
    for i in range(size):
        words += RandomChinaWord()
    return words

def send_file_via_api(token, channel_id, file_url, message=''):
    sleeptime = 5
    headers = {
        'Authorization': f'{token}',
    }

    files = {
        'file': ('fuckshit.txt', open('spam.txt', 'rb'))
    }

    payload = {
        'content': message
    }

    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    urlp = f"https://app.scrapingbee.com/api/v1/?api_key=8BO6CA3B9XSJWTVQZUYMCWN3M0IRV6AKIH2NFF66S1J0DCB9F22NMRE3WPOZCCZ6ZU7FNQGB6BG9ATYB&url={url}"
    response = requests.post(url, headers=headers, files=files, data=payload)

    if response.status_code == 200:
        print(f"\033[92m send message {response.status_code} \033[0m")
        time.sleep(1)
    else:
        print(f"\033[91m send failure send message {response.status_code} , sleep {sleeptime} second \033[0m")
        time.sleep(sleeptime)